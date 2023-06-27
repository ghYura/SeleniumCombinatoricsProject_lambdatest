import csv
import rstr
import re

is_ext_print = False
override_is_print = False
missed_param_mas = []
params_big = []

class Initial_text_input_data_preparation_1Str:#1st generated char is very important what it would be like
    def __init__(self, allowed_first_char="AZ", allowed_chars=r'a-z'):
        self.allowed_first_char = allowed_first_char#allowed_first_char = "AZ"
        self.allowed_chars = allowed_chars#allowed_chars = r'a-z'

    extrl_to_intrl = {"low_boundary_fixed": "low_boundary_fixed", "max": "max_length0", "min": "min_length0", "is_boundary_only": "is_boundary_only0_mode", "is_print": "is_print0"}
    def strtobool(val):#https://stackoverflow.com/a/18472142/11714800
        """Convert a string representation of truth to true (1) or false (0).
        True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
        are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
        'val' is anything else.
        """
        val = str(val).lower()
        if val in ('y', 'yes', 't', 'true', 'on', '1'):
            return True
        elif val in ('n', 'no', 'f', 'false', 'off', '0'):
            return False
        else:
            raise ValueError("invalid truth value %r" % (val,))

    def check_function_params(self, max_length0, min_length0=0, is_boundary_only0_mode=False, is_print0=False, explicit_params=None): #https://stackoverflow.com/a/58166804
        if is_ext_print: print("FYI: taken params:", max_length0, "|", min_length0, "|", is_boundary_only0_mode, "|", is_print0, "|'", explicit_params, "'-explicit_params")
        global missed_param_mas
        missed_param_mas = [True] *4
        b1, c1, d1 = [None, None, None]
        if 'min_length0' in explicit_params: b1 = min_length0
        else:
            if is_ext_print: print("2 parameter not given. Has no effect, but default")
            missed_param_mas[1] = False
        if 'is_boundary_only0_mode' in explicit_params: c1 = is_boundary_only0_mode
        else:
            if is_ext_print: print("3 parameter not given. Has no effect, but default")
            missed_param_mas[2] = False
        if 'is_print0' in explicit_params: d1 = is_print0
        else:
            if is_ext_print: print("4 parameter not given. Has no effect, but default")
            missed_param_mas[3] = False
        if b1 is None:
            b1 = min_length0
        if c1 is None:
            c1 = is_boundary_only0_mode
        if d1 is None:
            d1 = is_print0
        return Initial_text_input_data_preparation_1Str.make_input_values_list_in_range(b1, c1, d1)

    def make_input_values_list_in_range(self, max_length0, min_length0=0, is_boundary_only0_mode=False, is_print0=False):
        if is_ext_print: print("make_input_values_list_in_range(max_length0, min_length0=0, is_boundary_only0_mode=False, is_print0=False) <- ", max_length0, min_length0, is_boundary_only0_mode, is_print0)
        max_length0 = int(max_length0)
        min_length0 = int(min_length0)
        if isinstance(is_boundary_only0_mode, str): is_boundary_only0_mode = Initial_text_input_data_preparation_1Str.strtobool(is_boundary_only0_mode)
        if isinstance(is_print0, str): is_print0 = Initial_text_input_data_preparation_1Str.strtobool(is_print0)

        if min_length0 is None: min_length0=0
        if is_boundary_only0_mode is None: is_boundary_only0_mode=False
        if is_print0 is None: is_print0=False
        assert min_length0 >= 0
        assert max_length0 is not None
        assert isinstance(max_length0, int)
        assert max_length0 >= min_length0
        is_re_allowed_first_char = False
        is_re_allowed_chars = False
        try:
            re.compile(self.allowed_first_char)
            is_re_allowed_first_char = True
            if is_print0: print(f"Valid input regex-pattern: {self.allowed_first_char}")
        except re.error:
            is_re_allowed_first_char = False
            if is_print0: print(f"Invalid input regex-pattern: {self.allowed_first_char}")
        try:
            re.compile(self.allowed_chars)
            is_re_allowed_chars = True
            if is_print0: print(f"Valid input regex-pattern: {self.allowed_chars}")
        except re.error:
            is_re_allowed_chars = False
            if is_print0: print(f"Invalid input regex-pattern: {self.allowed_chars}")

        str_mas = []
        if is_boundary_only0_mode: step = max_length0 - min_length0 - 1
        else: step = 1
        if step == 0: step = 1
        max_length00 = max_length0
        if max_length0 - min_length0 == 1 or not is_boundary_only0_mode:
            max_length0 += 1

        for i in range(min_length0, max_length0, step):
            if is_print0: print(f"i) min_length0, max_length0, step, is_boundary_only| = {i}) {min_length0}, {max_length0}, {step}, {is_boundary_only0_mode}")
            if is_re_allowed_chars and (self.allowed_chars.startswith("[") and self.allowed_chars.endswith("}")): random_key = rstr.xeger(self.allowed_chars)
            else: random_key = rstr.xeger("["+str(self.allowed_chars)+"]{"+str(i)+"}")
            if is_print0: print(str(i) + "a)  random_key:", random_key)
            if self.allowed_first_char != "":
                if is_re_allowed_first_char:
                    if re.match(self.allowed_first_char, random_key[:1]): continue
                    else:
                        if (self.allowed_first_char.startswith("[") and self.allowed_first_char.endswith("]{1}"))\
                                or \
                           (self.allowed_first_char.startswith("(") and self.allowed_first_char.endswith("){1}")):
                            random_key = rstr.xeger(self.allowed_first_char) + random_key[1:]
                        else:
                            random_key = rstr.xeger("["+str(self.allowed_first_char)+"]{1}") + random_key[1:]
            if is_print0: print(str(i) + "b)  random_key:", random_key)
            if is_boundary_only0_mode and i == min_length0:

                if len(random_key) < min_length0:
                    while len(random_key) < min_length0:
                        if is_re_allowed_chars and (self.allowed_chars.startswith("[") and self.allowed_chars.endswith("}")): random_key += rstr.xeger(self.allowed_chars)
                        else: random_key += rstr.xeger("[" + str(self.allowed_chars) + "]{" + str(i) + "}")
                random_key = random_key[0:min_length0]
                if is_print0: print(">>>> random_key:", random_key)
                assert len(random_key) == min_length0

                random_key = random_key[0:min_length0] #TODO
                if is_print0: print(f"                                                           [is_boundary_only]-mode: min len(random_key) = {len(random_key)}")
                if is_print0: print(str(i) + "b1) random_key:", random_key)
            if is_boundary_only0_mode and i == max_length0-1:
                if max_length0 > max_length00: max_length0 = max_length00
                if len(random_key) < max_length0:
                    while len(random_key) < max_length0:
                        if is_re_allowed_chars and (self.allowed_chars.startswith("[") and self.allowed_chars.endswith("}")): random_key += rstr.xeger(self.allowed_chars)
                        else: random_key += rstr.xeger("[" + str(self.allowed_chars) + "]{" + str(i) + "}")
                    random_key = random_key[0:max_length0]
                assert len(random_key) == max_length0
                if is_print0: print(f"                                                           [is_boundary_only]-mode: max len(random_key) = {len(random_key)}")
                if is_print0: print(str(i) + "b2) random_key:", random_key)
            if is_print0: print(str(i) + "c)  random_key:", random_key)
            str_mas.append(random_key)

        if is_print0:
            print(f"                                                           returning final: len(str_mas)= {len(str_mas)}")
            for e in str_mas: print("                                                           e: "+str(e)+" |len(e)= "+str(len(e)))
        if not is_boundary_only0_mode and min_length0 == 0 and len(str_mas[0]) == len(str_mas[1]):
            if is_print0: print(f"workaround for 0-length: str_mas[0]={str_mas[0]}, str_mas[1]={str_mas[1]}")
            str_mas[0] = ""
        return str_mas

    with open(".\\FW_out.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            params = []
            if is_ext_print: print("row=", row)
            min000 = '0'
            for pv in row:
                params.append(pv)
                if pv.startswith("min"):
                    min000 = pv.split("=")[1]
            if is_ext_print: print("params=", params)
            params_big.append(params)
    for params in params_big:
        if is_ext_print: print(params)

    #CONTROL_PANEL
    #min = 0
    #max = 32
    #low_boundary_fixed=False
    #is_boundary_only=False
    #is_print=False
    #min00 = min
    #params = [max, min, is_boundary_only, is_print]
    @staticmethod
    def test_me():#tests this module (used with CONTROL_PANEL)
        min_re= re.compile(r'min=.*')# min00

        for params in params_big:

            min00 = '0'
            is_boundary_only = Initial_text_input_data_preparation_1Str.strtobool('False')

            if is_ext_print: print(f"1). params={params}")

            low_boundary_fixed = Initial_text_input_data_preparation_1Str.strtobool(str(params[:1][0]).split("=")[1])
            params = params[1:]
            if is_ext_print: print(f"2). params= {params}, low_boundary_fixed= {low_boundary_fixed}")

            max = int(str(params[0]).split("=")[1])
            params = params[1:]
            if is_ext_print: print(f"3). max= {max}, params= {params}, low_boundary_fixed= {low_boundary_fixed}")

            if any((match := min_re.search(item)) for item in params):
                if is_ext_print: print(f'At least one list item {match.group(0)} matches regex')
                min00 = match.group(0).split("=")[1]
            else:
                if is_ext_print: print(f'no list items match regex for min00 <- min= {min_re}')
                min00 = '0'
            min00 = int(min00)
            min = min00
            if is_ext_print: print(f"4). min00= {min00}, max= {max}, min= {min}, params={params}, low_boundary_fixed= {low_boundary_fixed}")

            params_dict = {}
            params_dict_extrl_to_intrl = {}
            for i in params:
                if is_ext_print: print("_"*30 + 'i.split("=")[0] +"="+ i.split("=")[1]  =  ', i.split("=")[0] +"="+ i.split("=")[1])
                params_dict[i.split("=")[0]] = i.split("=")[1]
                params_dict_extrl_to_intrl[Initial_text_input_data_preparation_1Str.extrl_to_intrl.get(i.split("=")[0])] = i.split("=")[1]

                if "is_boundary_only" == i.split("=")[0]:
                    is_boundary_only = i.split("=")[1]
                    is_boundary_only = Initial_text_input_data_preparation_1Str.strtobool(is_boundary_only)
                else:
                    is_boundary_only = 'False'
                    is_boundary_only = Initial_text_input_data_preparation_1Str.strtobool(is_boundary_only)

            if is_ext_print: print(f"5). min00= {min00}, max= {max}, params= {params}, low_boundary_fixed= {low_boundary_fixed}, is_boundary_only= {is_boundary_only}, params_dict= {params_dict}, params_dict_extrl_to_intrl= {params_dict_extrl_to_intrl}")

            while min <= max:
                if not override_is_print and Initial_text_input_data_preparation_1Str.extrl_to_intrl.get("is_print") in params_dict_extrl_to_intrl: params_dict_extrl_to_intrl[Initial_text_input_data_preparation_1Str.extrl_to_intrl.get("is_print")] = False #new
                if is_ext_print: print("low_boundary_fixed=", low_boundary_fixed)
                if is_ext_print: print("min=", min)
                if is_ext_print: print("max=", max)
                for _ in Initial_text_input_data_preparation_1Str.check_function_params(max, **params_dict_extrl_to_intrl):
                    print("result in return:", _)
                    if is_boundary_only: assert len(_) == min or len(_) == max
                if low_boundary_fixed: break
                else:
                    min += 1
                    if Initial_text_input_data_preparation_1Str.extrl_to_intrl.get("min") in params_dict_extrl_to_intrl:
                        if is_ext_print: print(params_dict_extrl_to_intrl)
                        params_dict_extrl_to_intrl[Initial_text_input_data_preparation_1Str.extrl_to_intrl.get("min")] = min #new
                    else:
                        if is_ext_print: print("#raise NotImplementedError")
                if min00 != min and not missed_param_mas[1]: break
                if max >= min and is_ext_print: print(f"========================================================================== [ increasing low boundary +1: min= {min} ]:")

#    test_me()#tests this module (used with CONTROL_PANEL)