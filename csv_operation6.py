#This module is "intermediate" (for my own self-educational purposes)
import copy
import itertools
import csv
from core7 import CoreCls
from selenium.webdriver.common.by import By

def through_csv_operation_call_core_dummy_send(generated_assimilated_strs_dict_to_mas_forwarding=None):
    el_to_xpath_dict = {'F':  "//input[@id='input-firstname']",
                        'L':  "//input[@id='input-lastname']",
                        '@':  "//input[@id='input-email']",
                        '#':  "//input[@id='input-telephone']",
                        'p':  "//input[@id='input-password']",
                        'd':  "//input[@id='input-confirm']",
                        'y':  "//input[@id='input-newsletter-yes']",
                        'n':  "//input[@id='input-newsletter-no']",
                        'V':  "//input[@id='input-agree']"
                        }
    generated_assimilated_strs_dict_to_mas_forwarding_stub = { #default-like well-known as 99%-to-be-passed as valid values in case, when generated and designed by QA-engineer data fail some-how-why
                        'F':  ["F"],
                        'L':  ["L"],
                        '@':  ["p1assthrough.g1uarantee@pr1ecleaned.i1n.d1b"],
                        '#':  ["+123"],
                        'p':  ["~!@#$%^&*()_+{}:\"|<>?-=[];'\\,./"],
                        'd':  ["~!@#$%^&*()_+{}:\"|<>?-=[];'\\,./"],
                        'y':  [None],
                        'n':  [None],
                        'V':  [None]
                        }
    if generated_assimilated_strs_dict_to_mas_forwarding is None: generated_assimilated_strs_dict_to_mas_forwarding = generated_assimilated_strs_dict_to_mas_forwarding_stub.copy()
    CoreCls.non_kbrd_els = ["y", "n", "V"] #non-keyboard elements keys for further click-action instead of key-actions for further keyboard "messing around entered text-boundaries"
    CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls = generated_assimilated_strs_dict_to_mas_forwarding_stub
    cor = CoreCls() #class itself (not its instance and not for multi-threading tests parallelization purposes) is used, due to single clipboard copy-paste-chars buffer on every this-test-code-execution machine, by far as I know
    cor.wd_ini() #webdriver initialization
    CoreCls.all_els = copy.deepcopy(el_to_xpath_dict)

    #PageObject placeholder and actual replacer due to any action-step is a combinatorial step in generated sequence:
    with open("F:\\FW_out.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        for row_from_csv in csvreader:
            print(row_from_csv)

            keys_list = list(generated_assimilated_strs_dict_to_mas_forwarding.keys())
            values_list = list(generated_assimilated_strs_dict_to_mas_forwarding.values())
            print("keys_list=", keys_list)
            print("values_list=", values_list)
            #<also, one more additional combinatorical stage, using local-code (this Python), that actually executes (to show advantages of "Combinatorics approach" in common sense)>:
            print("itertools.product(*keys_list)=", str(itertools.product(*list(generated_assimilated_strs_dict_to_mas_forwarding.values()))))
            #:</also, one more additional combinatorical stage, using local-code (this Python), that actually executes (to show advantages of "Combinatorics approach" in common sense)>
            for val in itertools.product(*values_list):
                #print("val=", val)
                print("TestCaseIdentifier:\n<<TC_" + str(row_from_csv) +"_"+ str(val)+"]/>>\n")#
                cor.fix_tries_n = 2 # <-- your value of fix-tries if smth. fails while reg-continue-button attempt
                for el_char in row_from_csv:
                    #print("el_char=", el_char)
                    CoreCls.cur_el = el_char
                    #<for my own self-educational purposes>:
                    # print(" outer call for cor.all_els=", cor.all_els)
                    # print(" outer call for CoreCls.all_els=", CoreCls.all_els)
                    #:</for my own self-educational purposes>
                    if el_char == 'F':
                        print("el_char='", el_char, "'=", str(val[0]))
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], str(val[0]), 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = str(val[0])
                        CoreCls.successful_non_complained_fields[el_char] = str(val[0]) # initial prefill
                    elif el_char == 'L':
                        print("el_char='", el_char, "'=", str(val[1]))
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], str(val[1]), 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = str(val[1])
                        CoreCls.successful_non_complained_fields[el_char] = str(val[1]) # initial prefill
                    elif el_char == '@':
                        print("el_char='", el_char, "'=", str(val[2]))
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], str(val[2]), 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = str(val[2])
                        CoreCls.successful_non_complained_fields[el_char] = str(val[2]) # initial prefill
                    elif el_char == '#':
                        print("el_char='", el_char, "'=", str(val[3]))
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], str(val[3]), 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = str(val[3])
                        CoreCls.successful_non_complained_fields[el_char] = str(val[3]) # initial prefill
                    elif el_char == 'p':
                        print("el_char='", el_char, "'=", str(val[4]))
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], str(val[4]), 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = str(val[4])
                        CoreCls.successful_non_complained_fields[el_char] = str(val[4]) # initial prefill
                    elif el_char == 'd':
                        print("el_char='", el_char, "'=", str(val[5]))
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], str(val[5]), 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = str(val[5])
                        CoreCls.successful_non_complained_fields[el_char] = str(val[5]) # initial prefill
                    elif el_char == 'y':
                        print("el_char='", el_char, "'=", "click")
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], None, 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = None
                        CoreCls.successful_non_complained_fields[el_char] = None # initial prefill
                    elif el_char == 'n':
                        print("el_char='", el_char, "'=", "click")
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], None, 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = None
                        CoreCls.successful_non_complained_fields[el_char] = None # initial prefill
                    elif el_char == 'V':
                        print("el_char='", el_char, "'=", "click")
                        cor.send_method(By.XPATH, el_to_xpath_dict[el_char], None, 0.001)
                        CoreCls.generated_assimilated_strs_dict_to_mas_forwarding_cls[el_char] = None
                        CoreCls.successful_non_complained_fields[el_char] = None # initial prefill
                    else:
                        raise NotImplementedError
                    cor.last_actn = None
                cor.continue_btn()
                cor.verification()
                cor.refresh()