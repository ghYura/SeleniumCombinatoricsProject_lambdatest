import rstr
import itertools

inp = "AthisisS"
one = '1'
two = '2'
three = '3'
kv_map = {'1': '0-9', '2': "0-9", '3': ''' \\]\\[!\\}@#$%^&*()_+=|'":;/\\.,<\\\\>~`\\{'''}

in_required_position_dict = {1: '0-9', 2: ''' \\]\\[!\\}@#$%^&*()_+=|'":;/\\.,<\\\\>~`\\{'''}
in_required_list = ['0-9', ''' \\]\\[!\\}@#$%^&*()_+=|'":;/\\.,<\\\\>~`\\{''', "3"]

def inp_to_outp(inp0, in_required_list1):
    inp_new0 = []
    #print("in_required_list1=", in_required_list1)
    if len(inp0) > len(in_required_list1):
        while len(inp0) > len(in_required_list1):
            in_required_list1.append(None)
    elif len(inp0) < len(in_required_list1):
        pass
    k0 = 0
    for e0 in inp0:
        if in_required_list1[k0] is None: inp_new0.append(e0)
        else: inp_new0.append(rstr.xeger("["+str(in_required_list1[k0])+"]{1}"))
        k0 += 1
    return inp_new0

def perm_spec_chars():
    strs_outp_big = []
    if len(inp) > len(in_required_list):
        in_required_list1 = [None] + list(in_required_list)
        while len(inp) > len(in_required_list1):
            in_required_list1.append(None)
    for perm in itertools.permutations(in_required_list1, r=None):
        #print("perm=", str(perm))
        i_t_o = inp_to_outp(inp, perm)
        strn = ''.join(map(str, i_t_o))
        #print("strn=", strn)
        strs_outp_big.append(strn)

def perm_spec_chars2(in_required_list0):
    lists_outp_big = []
    for perm in itertools.permutations(in_required_list0, r=None):
        #print("perm=", str(perm))
        lists_outp_big.append(list(perm))
    #print(lists_outp_big)
    return lists_outp_big

perm_spec_chars2(in_required_list)