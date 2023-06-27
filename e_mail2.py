from hypothesis import strategies
import exrex
import rstr
from typing import Literal, get_args

_TYPES = Literal["simple", "medium", "hard"]
_RE_LIBS = Literal["exrex", "rstr"]

def generate_email(limit=3, type_: _TYPES="simple", re_lib: _RE_LIBS="exrex", fyi=False):
    assert type_ in get_args(_TYPES), f"'{type_}' is not in {get_args(_TYPES)}"
    assert re_lib in get_args(_RE_LIBS), f"'{re_lib}' is not in {get_args(_RE_LIBS)}"
    r1_val = 1
    r2_val = 3

    if fyi: print("\nregHard:\n")
    regHard = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
    #regex_strategy = st.from_regex(str("r'")+str(reg)+str("'"), fullmatch=True)
    #regex_strategy = st.from_regex(reg, fullmatch=True)
    #print(regex_strategy.example())
    if fyi: print(exrex.getone(regHard))
    if fyi: print("")
    if fyi: print(exrex.getone(regHard))
    if fyi: print("")
    if fyi: print(exrex.getone(regHard))
    if fyi: print(">>>>>>>>>>")
    if fyi: print(rstr.xeger(regHard))

    if fyi: print("\nregmedium_RFC2821_RFC2822:\n")

    regSimple = r"([A-Za-z]){1}([0-9]){0,}[@]([A-Za-z]){1}([0-9]){0,}(\.([A-Za-z]){1,3}){1,2}"
    regmedium_RFC2821_RFC2822 = r"^((([!#$%&'*+\-/=?^_`{|}~\w])|([!#$%&'*+\-/=?^_`{|}~\w][!#$%&'*+\-/=?^_`{|}~\.\w]{0,}[!#$%&'*+\-/=?^_`{|}~\w]))[@]\w+([-.]\w+)*\.\w+([-.]\w+)*)$"
    regmedium_RFC2821_RFC2822_R1_R2 = r"^((([!#$%&'*+\-/=?^_`{|}~\w])|([!#$%&'*+\-/=?^_`{|}~\w][!#$%&'*+\-/=?^_`{|}~\.\w]{0,}[!#$%&'*+\-/=?^_`{|}~\w])){R1}[@](\w+([-.]\w+)*\.\w+([-.]\w+)*){R2})$"

    if fyi: print(exrex.getone(regmedium_RFC2821_RFC2822))
    if fyi: print("")
    if fyi: print(exrex.getone(regmedium_RFC2821_RFC2822))
    if fyi: print("")
    if fyi: print(exrex.getone(regmedium_RFC2821_RFC2822))

    #regex_strategy = strategies.from_regex(regmedium_RFC2821_RFC2822, fullmatch=True)
    #print(regex_strategy.example())
    if fyi: print("")
    if fyi: print(rstr.xeger(regmedium_RFC2821_RFC2822))

    regmedium_RFC2821_RFC2822_R1_R2_substituted = regmedium_RFC2821_RFC2822_R1_R2.replace("{R1}", "{"+str(r1_val)+"}")
    regmedium_RFC2821_RFC2822_R1_R2_substituted = regmedium_RFC2821_RFC2822_R1_R2_substituted.replace("{R2}", "{"+str(r2_val)+"}")

    if fyi and type_=="medium" and re_lib=="rstr": print("\nregmedium_RFC2821_RFC2822_R1_R2_substituted: ", regmedium_RFC2821_RFC2822_R1_R2_substituted, "\nrstr.xeger(regmedium_RFC2821_RFC2822_R1_R2_substituted) = ")
    if fyi and type_=="medium" and re_lib=="rstr": print(rstr.xeger(regmedium_RFC2821_RFC2822_R1_R2_substituted))
    if fyi and type_=="medium" and re_lib=="exrex": print("\nregmedium_RFC2821_RFC2822: ", regmedium_RFC2821_RFC2822, "\nexrex.getone(regmedium_RFC2821_RFC2822) = ")
    if fyi and type_=="medium" and re_lib=="exrex": print(exrex.getone(regmedium_RFC2821_RFC2822, limit=limit))
    if fyi: print("")
    if fyi and type_=="simple" and re_lib=="exrex": print("\nregSimple: ", regSimple, "\nexrex.getone(regSimple) = ")
    if fyi and type_=="simple" and re_lib=="exrex": print(exrex.getone(regSimple, limit=limit))
    if fyi: print("")

    if type_=="simple": rexp = regSimple
    elif type_=="medium": rexp = regmedium_RFC2821_RFC2822
    else: rexp = regHard

    if re_lib=="exrex": return exrex.getone(rexp, limit=limit)
    else: return rstr.xeger(rexp)

def gen_emails(start=3, step=1, maximum=10, fyi=True):
    emails_list = []
    while start <= maximum:
        emails_list.append(generate_email(start))
        start += step
    if fyi: print(emails_list)
    return emails_list