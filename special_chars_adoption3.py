import itertools
import math
import re
import string
import textwrap
from typing import Literal, get_args
import rstr

into = "AthisIsStringS"
strng = "123"
chars = set(string.ascii_lowercase)
chars = list(strng)
_TYPES = Literal["bigger", "ceil", "floor", "smaller"]
_SHIFTING = Literal["left", None, "right"]
_BOUNDARING = Literal["left", None, "right"]
what_list = ["0-9", re.escape(""" ][~!@#$%^&*()_+-={}:"|<>?,./\\;'"""), "3", "4", "5"]

def make_strings(head):
    remaining_chars = chars #- set(head)
    strings = [
        ''.join(tail)
        for tail in itertools.permutations(remaining_chars, len(remaining_chars))]
    return strings

def assimilate_chars(into, what_list0=None, type_: _TYPES = "floor", shift_: _SHIFTING = None, sep=''):#assimilate_chars(into, sep='-', _split = re.compile(str_dots+'?').findall):#https://stackoverflow.com/questions/3258573/how-to-insert-a-character-after-every-2-characters-in-a-string
    return_mas = []
    if what_list0 is None: what_list0=['']
    al_len = len(what_list0)#
    if type_=="ceil" or type_=="bigger":
        n_of_dots = math.ceil(float(len(into)) / float(len(what_list0)))#
        #print(f"n_of_dots = ceil(len(into) / len(what_list0)) = ceil( {len(into)} / {len(what_list0)} )=", math.ceil(float(len(into)) / float(len(what_list0))))
    elif type_=="floor" or type_=="smaller":
        n_of_dots = math.floor(float(len(into)) / float(len(what_list0)))#
        #print(f"n_of_dots = floor(len(into) / len(what_list0)) = floor( {len(into)} / {len(what_list0)} )=", math.floor(float(len(into)) / float(len(what_list0))))
    else: assert type_ in get_args(_TYPES), f"'{type_}' is not in {get_args(_TYPES)}"
    str_dots = str("."* n_of_dots)#
    _split = re.compile(str_dots+'?').findall#

    def inner_f(what_list00):
        what_list000 = []
        for adopted_char00 in what_list00:
            what_list000.append(rstr.xeger(r'[' + adopted_char00 + ']'))
        return what_list000

    #print("what_list0 (before)=", what_list0)
    what_list0 = inner_f(what_list0)
    #print("what_list0 (after)=", what_list0)

    c = 0
    counter = 1
    nofdotscounter = (n_of_dots * counter)

    if shift_ is None: shifter = 0
    else: shifter = 1

    intoX = list(into)
    while into[0] != what_list0[0]:
        counter = 1
        into = list(intoX)
        for adopted_char in what_list0:
            #print(f'(n_of_dots * counter) - shifter + c = ({n_of_dots * counter}) - {shifter} + {c} = {(n_of_dots * counter) - shifter + c}')
            if shift_ is None: into[n_of_dots * counter]=adopted_char
            elif shift_=="left": into[(n_of_dots * counter)-shifter + c]=adopted_char
            elif shift_=="right": into[(n_of_dots * counter)+shifter]=adopted_char
            else: assert shift_ in get_args(_SHIFTING), f"'{shift_}' is not in {get_args(_SHIFTING)}"
            if (counter<len(what_list0)): counter += 1
            if shift_ is not None: shifter += 1
        c += 1
        return_mas.append("".join(into))
        #print("return_mas=", return_mas)
        if shift_ is None: break
    return return_mas
def assimilate_chars2(into, what_list, is_shift=False, boundary_: _BOUNDARING = None):
    def regex_chars_to_chars(what_list00):
        what_list000 = []
        for adopted_char00 in what_list00:
            what_list000.append(rstr.xeger(r'[' + adopted_char00 + ']'))
        return what_list000
    #transformation:
    #print("what_list (before)=", what_list)
    what_list = regex_chars_to_chars(what_list)
    #print("what_list (after)=", what_list)
    #:transformation
    def adopt_chars_into_equally():
        per = len(what_list)
        #print("per=", str(per))
        txtwrp = textwrap.wrap(into, math.ceil(len(into) / len(what_list)))
        #print("txtwrp=", txtwrp)
        return txtwrp
    if boundary_ is not None:
        if boundary_ == "left":
            str_assimilated_left = ""
            into_list = list(into)
            into_list[1:1+len(what_list)] = what_list
            for e in into_list:
                str_assimilated_left += "".join(e)
            return str_assimilated_left
        elif boundary_ == "right":
            str_assimilated_right = ""
            into_list = list(into)
            into_list[len(into_list)-len(what_list):len(into_list)] = what_list
            for e in into_list:
                str_assimilated_right += "".join(e)
            return str_assimilated_right
        else: assert boundary_ in get_args(_BOUNDARING), f"'{boundary_}' is not in {get_args(_BOUNDARING)}"
    else: equalized_adoption = adopt_chars_into_equally()
    new_chars_collection = []
    k = 0
    shift = 1
    for chnk in equalized_adoption:
        chnk = list(chnk)
        if is_shift: chnk[len(chnk)-1-shift] = what_list[k]
        else: chnk[len(chnk)-1] = what_list[k]
        new_chars_collection.append("".join(chnk))
        k += 1
    str_assimilated = ""
    for a in new_chars_collection:
        str_assimilated += "".join(str(a))
    return str_assimilated
def main():
    #print("into=", into)
    str_a1 = assimilate_chars2(into, what_list)
    #print("str_a1=", str_a1)
    str_a2_shifted = assimilate_chars2(into, what_list, is_shift=True)
    #print("str_a2_shifted=", str_a2_shifted)
    str_a3_boundary_left = assimilate_chars2(into, what_list, boundary_="left")
    #print("str_a3_boundary_left=", str_a3_boundary_left)
    str_a3_boundary_right = assimilate_chars2(into, what_list, boundary_="right")
    #print("str_a3_boundary_right=", str_a3_boundary_right)
    strs_assimilated_mas = [str_a1, str_a2_shifted, str_a3_boundary_left, str_a3_boundary_right]
    #print("strs_assimilated_mas=", strs_assimilated_mas)
    intos = [into]*4
    #print("intos=               ", intos)

    gentr = list(itertools.permutations(strng, len(strng)))
    perm_str_mas_res = []
    perm_none_list = []
    for perm_tup in gentr:
        flag = False
        p1_none_p2_list = []
        for p in list(perm_tup):
            if not flag:
                p1_none_p2_list.append(None)
                p1_none_p2_list.append(p)
            else:
                p1_none_p2_list.append(None)
                p1_none_p2_list.append(p)
            flag = True
        perm_none_list.append(p1_none_p2_list)

        perm_str_mas_res.append(''.join((perm_tup)))
    #print(perm_str_mas_res)
    #print(len(perm_str_mas_res))
    #print(perm_none_list)
    #print(len(perm_none_list))

if __name__ == '__main__':
    main()