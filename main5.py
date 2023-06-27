import re
import e_mail2
import initial_text_input_data_preparation_1str1
import permutate_spec_chars4
import special_chars_adoption3

is_print = False #log-level-alike for this test-code

into_first_name_first_char = "AZ" #important start 1st initial char in FirstName txt-input field (if code-under-test, as "testing object", watches every single user's action) for further watch reaction (and possible delay after it's entered)
into_first_name_allowed_chars = r"a-z" #rest of the chars in this input field
into_first_name_min_range = 1 #given boundary limitation for field (according to SDesignS-SRS)
into_first_name_max_range = 32 #given boundary limitation for field (according to SDesignS-SRS)
what_list_first_name = ["0-9", re.escape("""][~!@#$%^&*()_+={}:"|<>?,/\\;'"""), "-", ".", " "] #special chars (as by provocation scenario-testCase or by SDesignS-SRS) here parameterized by QA-engineer wants to be adopted into txt-input field
into_last_name_first_char = into_first_name_first_char
into_last_name_allowed_chars = into_first_name_allowed_chars
into_last_name_min_range = 1
into_last_name_max_range = 32
what_list_last_name = what_list_first_name
#<e-mail>:
e_m = e_mail2.generate_email()
#:</e-mail>
into_phone_number_first_char = re.escape("+")
into_phone_number_allowed_chars = r"0-9"
into_phone_number_min_range = 3
into_phone_number_max_range = 32
what_list1_phone_number = ["-", "(", ")", "-", "-", "-"] #phone number punctuation mask (variant1)
what_list2_phone_number = [".", "(", ")", ".", ".", "."] #phone number punctuation mask (variant2)
what_list3_phone_number = [" ", "(", ")", " ", " ", " "] #phone number punctuation mask (variant3)
into_password1_first_char = ""
into_password1_allowed_chars = re.escape("""][~!@#$%^&*()_+={}:"|<>?,/\\;'""")
into_password1_min_range = 4
into_password1_max_range = 20
what_list_password1 = [r"A-Za-z0-9 "]
into_password2_first_char = into_password1_first_char
into_password2_allowed_chars = into_password1_allowed_chars
into_password2_min_range = into_password1_min_range
into_password2_max_range = into_password1_max_range
what_list_password2 = what_list_password1

what_list = ["0-9", re.escape("""][~!@#$%^&*()_+={}:"|<>?,/\\;'"""), "-", ".", " "]

def adopt_spec_chars(into0, what_list0):
    str_a1 = special_chars_adoption3.assimilate_chars2(into0, what_list0)
    str_a2_shifted = special_chars_adoption3.assimilate_chars2(into0, what_list0, is_shift=True)
    str_a3_boundary_left = special_chars_adoption3.assimilate_chars2(into0, what_list0, boundary_="left")
    str_a3_boundary_right = special_chars_adoption3.assimilate_chars2(into0, what_list0, boundary_="right")
    strs_assimilated_mas = [str_a1, str_a2_shifted, str_a3_boundary_left, str_a3_boundary_right]
    intos = [into0] * 4
    return strs_assimilated_mas

def prepare_text_field_data_as_list(into_first_char0, into_allowed_chars0, into_min_range0, into_max_range0, what_list0):
    initial_1str_cls_initialized = initial_text_input_data_preparation_1str1.Initial_text_input_data_preparation_1Str(into_first_char0, into_allowed_chars0)
    initial_strs = initial_1str_cls_initialized\
        .make_input_values_list_in_range(max_length0=into_max_range0,
                                         min_length0=into_min_range0,
                                         is_boundary_only0_mode=True,
                                         is_print0=False)
    if is_print: print(initial_strs)
    total_output = []
    permutated_spec_chars_list = permutate_spec_chars4.perm_spec_chars2(what_list0)
    if is_print: print("permutated_spec_chars_list=", permutated_spec_chars_list)
    for ini in initial_strs:
        flag_is_duplicate = False
        for perm in permutated_spec_chars_list:
            if is_print: print("perm=", perm)
            if len(ini) > len(perm): strs_assimilated_mas = adopt_spec_chars(ini, perm)
            else:
                if is_print: print("ini=", ini)
                if not flag_is_duplicate: strs_assimilated_mas = [ini]
                else: flag_is_duplicate = True
            if is_print: print("strs_assimilated_mas=", strs_assimilated_mas)

            total_output = total_output + (list(strs_assimilated_mas))
            # removing duplicates, if 'flag_is_duplicate' fails somehow; and second refinery, if permutation and further assimilation fails:
            total_output = list(dict.fromkeys(total_output))
    print("initial_strs=", initial_strs)
    print("total_output=", total_output)
    print("len(total_output)=", len(total_output))
    return total_output

def main():

    fn_list = prepare_text_field_data_as_list(
        into_first_name_first_char,
        into_first_name_allowed_chars,
        into_first_name_min_range,
        into_first_name_max_range,
        what_list_first_name
    )
    ln_list = prepare_text_field_data_as_list(
        into_last_name_first_char,
        into_last_name_allowed_chars,
        into_last_name_min_range,
        into_last_name_max_range,
        what_list_last_name
    )
    em_list = e_mail2.gen_emails()
    phn_list = prepare_text_field_data_as_list(
        into_phone_number_first_char,
        into_phone_number_allowed_chars,
        into_phone_number_min_range,
        into_phone_number_max_range,
        what_list1_phone_number
    )
    phn_list.extend(
        prepare_text_field_data_as_list(
            into_phone_number_first_char,
            into_phone_number_allowed_chars,
            into_phone_number_min_range,
            into_phone_number_max_range,
            what_list2_phone_number
        )
    )
    phn_list.extend(
        prepare_text_field_data_as_list(
            into_phone_number_first_char,
            into_phone_number_allowed_chars,
            into_phone_number_min_range,
            into_phone_number_max_range,
            what_list3_phone_number
        )
    )
    p1_list = prepare_text_field_data_as_list(
        into_password1_first_char,
        into_password1_allowed_chars,
        into_password1_min_range,
        into_password1_max_range,
        what_list_password1
    )
    p2_list = p1_list.copy()

    el_to_text_list_dict = {'F': fn_list,
                            'L': ln_list,
                            '@': em_list,
                            '#': phn_list,
                            'p': p1_list,
                            'd': p2_list,
                            'y': [None],#non-txt input field for further click, instead of typing-in
                            'n': [None],#non-txt input field for further click, instead of typing-in
                            'V': [None] #non-txt input field for further click, instead of typing-in
                           }
    print("el_to_text_list_dict=", el_to_text_list_dict)

    #<data and logic "forwarding" programming-test-self-learning my coding feature>:
    import csv_operation6
    csv_operation6.through_csv_operation_call_core_dummy_send(generated_assimilated_strs_dict_to_mas_forwarding=el_to_text_list_dict)
    #:</data and logic "forwarding" programming-test-self-learning my coding feature>

if __name__ == "__main__":
    main()