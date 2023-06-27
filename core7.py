#NOTE: this whole module's code could be used into input xlsx-file for Combinatorics Framework, where its user decides,
#"where" to decompose to combinatorial unit, or where to put optional part whatever code needed as 'FW_Optional'(similar to random-like logic 'semi-chance-coin-toss', but '99% guaranteed as to-be-passed-through')
#in combinations with obligatory part(s)
#and as the output - you'll get a bunch of modules or composed of many functional-parts single module
#For decomposition details example, please refer to 'HTTPjsonPlaceholder' site test Video.
#In a nutshell:
# Create your own combi-situational TestCases as so as combined-composed-code out of criteria-matching-situation according to your code or case requirements
# Pick this code pieces and create your own with sudden optional actions wherever you want-need and interesting for you code combinations-permutations
# Combinatorics Framework initial author, Yurii Baranov from Kiev, Ukraine, with respect to all initial genuine Authors of all Good things and ideas
# All registered Any Marks belong to their owner

import random
import re
import sys
import time
import rstr
from tkinter import Tk, TclError
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from collections import OrderedDict
import pyperclip as pc
from typing import Literal, get_args

import e_mail2

# common actions for messing around in text input field:
_ACTIONS = Literal["copyCharAt", "pasteCharAt", "replaceCharAt", "deleteCharAt",
                   "copyAll", "deleteAll", "pasteAllAt", "selectAll", "click",
                   "moveLeft", "moveRight"]

d = 0 # for further digit_uniqificator() for text input filed
invalid_phone_msg = None
fix_tries_n = 2 # initial for this module
provocation_coin_toss = False
class CoreCls:
    successful_non_complained_fields = {} # placeholder for further test-development for given situation (if some field keeps complaining somewhy)
    generated_assimilated_strs_dict_to_mas_forwarding_stub_cls = {}
    generated_assimilated_strs_dict_to_mas_forwarding_cls = {}
    fix_input_and_reg_continue_button = True
    pass_flag = False # exit criteria for test for given combination (QA-engineer furter in this code manipulates its value)
    reuse_failed_reg_page_mode = False
    cur_el = None # current webelement key (class' field here)
    all_els = OrderedDict()
    non_kbrd_els = []
    last_actn = None # TODO: for furher test-development
    options = Options() # Browser options:
    options.page_load_strategy = 'normal'
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    max_default_timeout00 = 1000000 # TODO: for further test-development. timeout for whole word typing
    halt = False # TODO: for futher test-development sudden switch to other input field with what-characters-left ('slice_left00') to enter in that newly-switched field
    slice_left00 = "" # TODO: for futher test-development sudden switch to other input field with what-characters-left. Uses with 'halt'
    cb_content = "" # clipboard content

    @classmethod
    def wd_ini(cls):
        cls.browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        max_default_timeout00 = 1000000
        halt = False
        cls.browser.set_page_load_timeout(5)
        cls.pass_flag = False

    #def __init__(self):
    #    pass

    @staticmethod
    def clipboard_content(): # currently obsoleted method
        while True:
            try:
                cb_content_ = Tk().clipboard_get()
                print("Clipboard content triggered: <<cb_content_>>", cb_content_, "<</cb_content_>>")
                if cb_content_ is not None and cb_content_ != "":
                    cb_content = cb_content_
                    break
                sleep(0.1)
            except TclError:
                # print("Clipboard is empty.")
                sleep(0.1)
        if cb_content_ is not None and cb_content_ != "":
            pd.io.clipboard.clipboard_set(cb_content_)

    @classmethod
    def keyboard_manipulator(cls, by0, locator_str0, new_chars=None, delay0=0.0, cursor_pos=0, clicked_once=False, common_action_: _ACTIONS="click"):
        cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        assert common_action_ in get_args(_ACTIONS), f"'{common_action_}' is not in {get_args(_ACTIONS)}"
        if by0 == By.ID:
            el = cls.browser.find_element(by0, locator_str0)
        elif by0 == By.XPATH:
            el = WebDriverWait(cls.browser, 100).until(lambda browser: cls.browser.execute_script('return document.readyState') == 'complete')
            el = cls.browser.find_element(by0, value=locator_str0)
        else:
            raise NotImplementedError
        if common_action_ == "click":
            try:
                el.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                print("FAIL# Direct click by Xpath or Id - unavaiable. Click Intercepted. Workaround through js-script")
                cls.browser.execute_script("arguments[0].click();", el)
        else:
            entered_before_chars = str(el.get_attribute("value"))
            print(f'entered_before_chars = "{entered_before_chars}"')

            if not clicked_once:
                try:
                    el.click()
                except selenium.common.exceptions.ElementClickInterceptedException:
                    print("FAIL# Direct click by Xpath or Id - unavaiable. Click Intercepted. Workaround through js-script")
                    cls.browser.execute_script("arguments[0].click();", el)
                clicked_once=True
            if new_chars is not None: pc.copy(str(new_chars))
            if common_action_ == "pasteCharAt":
                ActionChains(cls.browser).send_keys(Keys.HOME).perform()
                init_cursor_pos=0
                while init_cursor_pos != cursor_pos:
                    ActionChains(cls.browser).pause(delay0).send_keys(Keys.HOME).perform()
                    init_cursor_pos += 1
                ActionChains(cls.browser).pause(delay0).key_down(cmd_ctrl).pause(delay0).send_keys("v").pause(delay0).key_up(cmd_ctrl).perform()
            elif common_action_ == "copyCharAt":
                ActionChains(cls.browser).send_keys(Keys.HOME).perform()
                init_cursor_pos = 0
                while init_cursor_pos != cursor_pos:
                    ActionChains(cls.browser).pause(delay0).send_keys(Keys.HOME).perform()
                    init_cursor_pos += 1
                ActionChains(cls.browser).pause(delay0).key_down(Keys.SHIFT).pause(delay0).send_keys(Keys.ARROW_RIGHT).pause(delay0).key_up(Keys.SHIFT).pause(delay0).key_down(cmd_ctrl).pause(delay0).send_keys("c").pause(delay0).key_up(cmd_ctrl).perform()
            elif common_action_ == "deleteCharAt":
                ActionChains(cls.browser).send_keys(Keys.HOME).perform()
                init_cursor_pos = 0
                while init_cursor_pos != cursor_pos:
                    ActionChains(cls.browser).pause(delay0).send_keys(Keys.HOME).perform()
                    init_cursor_pos += 1
                ActionChains(cls.browser).pause(delay0).send_keys(Keys.DELETE).perform()
            elif common_action_ == "replaceCharAt":
                ActionChains(cls.browser).send_keys(Keys.HOME).perform()
                init_cursor_pos = 0
                while init_cursor_pos != cursor_pos:
                    ActionChains(cls.browser).pause(delay0).send_keys(Keys.HOME).perform()
                    init_cursor_pos += 1
                ActionChains(cls.browser).pause(delay0).key_down(Keys.SHIFT).pause(delay0).send_keys(Keys.ARROW_RIGHT).pause(delay0).key_up(Keys.SHIFT).pause(delay0).key_down(cmd_ctrl).pause(delay0).send_keys("v").pause(delay0).key_up(cmd_ctrl).perform()
            elif common_action_ == "copyAll":
                cls.keyboard_manipulator(by0, locator_str0, new_chars, delay0, cursor_pos, clicked_once, common_action_="selectAll")
                ActionChains(cls.browser).pause(delay0).key_down(cmd_ctrl).pause(delay0).send_keys("c").pause(delay0).key_up(cmd_ctrl).perform()
                time.sleep(1)
                buffer_content = pc.paste()
                print(f'entered_before_chars = "{entered_before_chars}" ?= "{buffer_content}" =buffer_content')
                try:
                    assert entered_before_chars == buffer_content
                except AssertionError:
                    print("FAIL wrong clipboard buffer content. Was trying to copyAll in the field")
                    print(f'entered_before_chars = "{entered_before_chars}" ?= "{buffer_content}" =buffer_content')
                finally:
                    print("returning clipboard content back from analysis")
                    pc.copy(buffer_content)
            elif common_action_ == "selectAll":
                ActionChains(cls.browser).pause(delay0).key_down(cmd_ctrl).pause(delay0).send_keys("a").pause(delay0).key_up(cmd_ctrl).perform()
            elif common_action_ == "deleteAll":
                cls.keyboard_manipulator(by0, locator_str0, new_chars, delay0, cursor_pos, clicked_once, common_action_="selectAll")
                ActionChains(cls.browser).pause(delay0).send_keys(Keys.DELETE).pause(delay0).perform()
                if by0 == By.ID:
                    el = cls.browser.find_element(by0, locator_str0)
                elif by0 == By.XPATH:
                    el = WebDriverWait(cls.browser, 100).until(
                        lambda browser: cls.browser.execute_script('return document.readyState') == 'complete')
                    el = cls.browser.find_element(by0, value=locator_str0)
                else: raise NotImplementedError
                print('el.get_attribute("value")=', el.get_attribute("value"))
                try:
                    assert len(str(el.get_attribute("value"))) == 0
                except AssertionError:
                    print(f"FAIL# wrong tag attribute value. Expected another according to action '{common_action_}'")
            elif common_action_ == "moveLeft": ActionChains(cls.browser).pause(delay0).send_keys(Keys.ARROW_LEFT).pause(delay0).perform()
            elif common_action_ == "moveRight": ActionChains(cls.browser).pause(delay0).send_keys(Keys.ARROW_RIGHT).pause(delay0).perform()
            else: print(f"common_action_ == {common_action_} - Unsupported or not implemented yet.")
        last_actn = str(common_action_)

    @classmethod
    def send_method(cls, by0, locator_str0, word0, delay0, delay_randomly0=False, timeout0=max_default_timeout00):
        #<for my own self-educational purposes>:
        # print("send_method() triggered!")
        # print("all_els=", cls.all_els)
        #:</for my own self-educational purposes>
        slice_left00 = ""
        el = None

        if by0 == By.ID:
            el = cls.browser.find_element(by0, locator_str0)
        elif by0 == By.XPATH:
            el = WebDriverWait(cls.browser, 100).until(lambda browser: cls.browser.execute_script('return document.readyState') == 'complete')
            el = cls.browser.find_element(by0, value=locator_str0)
        else:
            raise NotImplementedError
        slice_left = slice_left00
        if delay_randomly0 is True:
            assert delay0 >= 1
        assert timeout0 > 0
        delay_mas = []

        if word0 is None:
            el = WebDriverWait(cls.browser, 10).until(EC.presence_of_element_located((by0, locator_str0)))
            cls.browser.execute_script("arguments[0].click();", el)
        else:
            delta0 = float(timeout0) / float(len(word0))
            if timeout0 < 1000000:
                if delay_randomly0:
                    delta2 = 0
                    while len(delay_mas) < len(word0):
                        x1 = delta0 + delta2
                        assert x1 > 0
                        x2 = random.Random.random()
                        delta = x1 - x2
                        assert delta > 0
                        delay_mas.append(delta)
                        delta2 = x2 + delta
                        assert delta2 > 0
                    total = 0
                    for i in range(len(delay_mas)):
                        total += delay_mas[i]
                    assert total <= timeout0, f"total = {total} > {timeout0} = timeout"
                elif not delay_randomly0:
                    while len(delay_mas) < len(word0):
                        delay_mas.append(delta0)
                    total = 0
                    for i in range(len(delay_mas)):
                        total += delay_mas[i]
                    assert total <= timeout0, f"total = {total} > {timeout0} = timeout"
            else:
                while len(delay_mas) < len(word0):
                    delay_mas.append(delay0)
            chars_in_word = list(word0)
            assert len(chars_in_word) == len(delay_mas)
            counter = 0
            timeout = timeout0
            for j in range(len(chars_in_word)):
                c = chars_in_word[j]
                if by0 == By.ID:
                    cls.browser.find_element(by0, locator_str0).send_keys(c)
                elif by0 == By.XPATH:
                    cls.browser.find_element(by0, value=locator_str0).send_keys(c)
                else:
                    raise NotImplementedError
                counter += 1
                slice_left = chars_in_word[counter:len(chars_in_word)]
                if cls.halt:
                    break
                if delay_randomly0 and timeout0 == 1000000:
                    if isinstance(delay0, int): slp = random.Random.randint(0, delay0)
                    else: slp = random.uniform(0, delay0)
                    sleep(slp)
                    timeout = timeout - slp
                else:
                    sleep(delay_mas[j])
                    timeout = timeout - delay_mas[j]
            assert timeout >= 0

            return slice_left, timeout

    @classmethod
    def sudden_action1(cls): # lots of other sudden ('optional' in terms of Combinatorics framework) action could be described and be generated and called from any row of code. Their control and affection on object-under-test and test-code (by variables?) supposed to be delegated to QA-testCase-engineer-designer
        # particularly this sudden action responsible for user's "messing around" by keyboard keys at 1st and last characters in text input field.
        print(f"successful_non_complained_fields = {cls.successful_non_complained_fields}")
        by0 = By.XPATH
        #cls.cur_el
        for cur_e in cls.successful_non_complained_fields.keys():# for cur_e in cls.all_els.keys():
            if not cls.pass_flag:  #
                if cls.successful_non_complained_fields[cur_e] == "complained":#cur_val = cls.all_els[cur_e]
                    cur_val = cls.all_els[cur_e]#cur_val = cls.all_els[cur_e]
                    #
                    print(f"=========cls.successful_non_complained_fields = {cls.successful_non_complained_fields}")
                    print("cur_e='", cur_e, "' cur_val=", cur_val)
                    locator_str0 = cur_val
                    if by0 == By.ID:
                        el = cls.browser.find_element(by0, locator_str0)
                    elif by0 == By.XPATH:
                        el = WebDriverWait(cls.browser, 100).until(
                            lambda browser: cls.browser.execute_script('return document.readyState') == 'complete')
                        el = cls.browser.find_element(by0, value=locator_str0)
                    else:
                        raise NotImplementedError

                    some_flag_saying_for_elements_with_text_value = False
                    try:
                        print(f" el.text='{el.text}'")
                        some_flag_saying_for_elements_with_text_value = True
                    except Exception as e:
                        print(f" something went wrong! - {e}")
                        try:
                            print(" el.get_attribute(value)=", el.get_attribute("value"))
                            some_flag_saying_for_elements_with_text_value = True
                        except Exception as e:
                            print(f" something went wrong! - {e}")
                        finally:
                            print(" finally1")
                    finally:
                        print(" finally2")
                        # workaround for elements without text-values tags
                    for actn in list(get_args(_ACTIONS)):
                        if not cls.pass_flag:#
                            print(" actn:", actn)
                            print(f" cls.non_kbrd_els='{cls.non_kbrd_els}', cur_e='{cur_e}', intentionally set cur_el=cur_e ")
                            cls.cur_el = cur_e
                            if not some_flag_saying_for_elements_with_text_value or cls.non_kbrd_els.__contains__(cur_e):
                                cls.keyboard_manipulator(by0, locator_str0, new_chars=None, delay0=0.1, cursor_pos=0, clicked_once=False, common_action_="click")
                                cls.warning_msg_finder_and_resolver()#
                                cls.continue_btn()
                                cls.verification_desperate()
                                break
                            else:
                                for pos in [0, len(cls.browser.find_element(by0, value=locator_str0).get_attribute("value"))]:
                                    if not cls.pass_flag:#
                                        el = WebDriverWait(cls.browser, 20).until(EC.presence_of_element_located((by0, locator_str0)))#el = cls.browser.find_element(by0, value=locator_str0)

                                        print(f"messing around near {pos} position in text-field...")
                                        if cur_e == "@":#
                                            cls.browser.find_element(by0, locator_str0).clear()#
                                            cls.keyboard_manipulator(by0, locator_str0, new_chars=e_mail2.generate_email(limit=random.randint(3, 10)), delay0=0.1, cursor_pos=pos, clicked_once=False, common_action_=actn) #
                                        else:#
                                            cls.keyboard_manipulator(by0, locator_str0, new_chars=rstr.xeger(r'.'), delay0=0.1, cursor_pos=pos, clicked_once=False, common_action_=actn)
                                        #cls.successful_non_complained_fields[cls.cur_el] = cls.browser.find_element(by0, value=locator_str0).get_attribute("value")
                                        print(f'______________ cls.successful_non_complained_fields[cls.cur_el] ->[{str(cls.cur_el)}] = cls.browser.find_element(by0, value=locator_str0).get_attribute("value") = {cls.browser.find_element(by0, value=locator_str0).get_attribute("value")}')
                                        cls.warning_msg_finder_and_resolver()#
                                        cls.continue_btn()
                                        cls.verification_desperate()
                            #

    @classmethod
    def sudden_clear_of_non_complained_fields(cls): #
        print(f"Prior to clear of non-complained fields, Are there any 'complained' at all?:\n {cls.successful_non_complained_fields}")

        for no_cmpln in cls.successful_non_complained_fields.keys():
            if cls.successful_non_complained_fields[no_cmpln] is not None and not cls.pass_flag \
                    and cls.successful_non_complained_fields[no_cmpln] != "complained":
                print(f"cleaning non-complained field '{str(no_cmpln)}'")
                if not cls.non_kbrd_els.__contains__(cls.all_els[no_cmpln]): WebDriverWait(cls.browser, 10).until(EC.presence_of_element_located((By.XPATH, cls.all_els[no_cmpln])))#time.sleep(1)
                if not cls.non_kbrd_els.__contains__(cls.all_els[no_cmpln]): cls.browser.find_element(By.XPATH, cls.all_els[no_cmpln]).clear()
                else:
                    try:
                        cls.browser.find_element(By.XPATH, cls.all_els[no_cmpln]).click()
                    except selenium.common.exceptions.ElementClickInterceptedException:
                        print("Here we would ignore 'element click intercepted' somewhy, but for furter to fail test")
                cls.continue_btn()  #
                cls.verification_desperate()  #


    @classmethod
    def continue_btn(cls):
        cls.browser.find_element(By.XPATH, value="//input[@value='Continue']").click()
        time.sleep(0.1)

    @classmethod
    def verification_desperate(cls):
        try:
            assert cls.browser.title == "Your Account Has Been Created!"
            cls.pass_flag = True
            print("\n[PASS]\n" + str("=" * 100))
        except AssertionError:
            cls.pass_flag = False

    @classmethod
    def verification(cls):
        global invalid_phone_msg
        global fix_tries_n
        global provocation_coin_toss
        email_registered_msg = None

        try:
            assert cls.browser.title == "Your Account Has Been Created!"
            print("\t\t\t\t[FYI]: placeholder where test-code goes to DB and verifies this newly created account")
            print("\n[PASS]\n"+str("="*100))
            fix_tries_n = 2

            cls.pass_flag = True # test exit criteria (whatever actions taken - this is the goal. However, entered passed-through-fields have to be memorized further and post-analyzed as valid or as interesting-how-could-they-be-passed-through)
        except AssertionError:
            cls.pass_flag = False
            # print("<SUDDEN ACTION1: to play keboard keys against every text field>")
            # cls.sudden_action1()
            # print("</SUDDEN ACTION1: to play keboard keys against every text field>")
            print("FAIL 1. No success title for registration")
            print("Looking for a reason on the page...")
            while fix_tries_n > -1 and cls.pass_flag is False:
                provocation_coin_toss = bool(random.getrandbits(1)) # placeholder: instead of random with semi-guaranteed of sudden action, here could be 'FW_Optional' but guaraneed action for every generated combination
                cls.warning_msg_finder_and_resolver()
                print(f"fix_tries_n = {fix_tries_n}, cls.pass_flag = {cls.pass_flag}")
                time.sleep(1)
                #provocation_coin_toss = bool(random.getrandbits(1)) # placeholder: instead of random with semi-guaranteed of sudden action, here could be 'FW_Optional' but guaraneed action for every generated combination
                if provocation_coin_toss:
                    print("<SUDDEN ACTION2: provocation_coin_toss -->> sudden_clear_of_non_complained_fields()>")
                    cls.sudden_clear_of_non_complained_fields() # placeholder: instead of random with semi-guaranteed of sudden action, here could be 'FW_Optional' but guaraneed action for every generated combination
                    print("</SUDDEN ACTION2: provocation_coin_toss -->> sudden_clear_of_non_complained_fields()>")
                    provocation_coin_toss = False # obligatory to set flag to initial 'False'
                cls.continue_btn()
                fix_tries_n -= 1
                cls.verification()
            if fix_tries_n < 0:
                print("<SUDDEN ACTION1: to play keboard keys against every text field>")
                cls.sudden_action1()
                print("</SUDDEN ACTION1: to play keboard keys against every text field>")
                if not cls.pass_flag: print("[FAIL]      "*10 +"\neven after all fix tries")
                fix_tries_n = 2
                print("-"*100)


    @classmethod
    def refresh(cls):
        if cls.reuse_failed_reg_page_mode and not cls.pass_flag:
            print(f"\n[FYI] reuse_failed_reg_page_mode = {cls.reuse_failed_reg_page_mode} and previous test FAILED\n(search in rolling console or log for FAIL-tags as fail-confirm state). \nPage refresh skipped\n")
        else:
            try:
                cls.browser.find_element(By.LINK_TEXT, "Logout").click()
            except NoSuchElementException or selenium.common.exceptions.TimeoutException:
                print("element not found and waiting for it - timed out")
            finally:
                cls.browser.refresh()
                cls.wd_ini()

    @classmethod
    def refresh0(cls):# obsoleted
        cls.browser.refresh()
        cls.wd_ini()

    @classmethod
    def digit_uniqificator(cls, inp=""):
        global d
        d_to_return = d
        d += 1
        return inp+str(d_to_return)

    @classmethod
    def replace_str_index(cls, text, index=0, replacement=''):
        return f'{text[:index]}{replacement}{text[index + 1:]}'

    @classmethod
    def warning_msg_finder_and_resolver(cls):
        print(f"fix_tries_n = {fix_tries_n}")
        email_already_registered_msg = None # initial value
        try:
            # since it finds higher-level div-tag with class='mz-pure-container' email_already_registered_msg = cls.browser.find_element(By.XPATH, "//div[contains(string(), ' Warning: E-Mail Address is already registered!')]")
            email_already_registered_msg = cls.browser.find_element(By.XPATH, "//div[contains(text(), ' Warning: E-Mail Address is already registered!')]")
            print(f' email_already_registered_msg.text = {email_already_registered_msg.text}, email_already_registered_msg2.get_attribute("class") = {email_already_registered_msg.get_attribute("class")}')
            print(" email_already_registered_msg=", email_already_registered_msg)
            cls.successful_non_complained_fields["@"] = "complained" # placeholder for further test-development for given situation
            print("'complained' value set for '@'")
        except NoSuchElementException:
            print(" not found email_already_registered_msg")
        try:
            sleep(1)
            warn_e_under_breadcrumbs = cls.browser.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]')
            if email_already_registered_msg is not None:
                print(" str(email_already_registered_msg.get_attribute('class')) = ", str(email_already_registered_msg.get_attribute("class")))
                assert str(email_already_registered_msg.get_attribute("class")) == "alert alert-danger alert-dismissible"
                print(' email_already_registered_msg.get_attribute("class")=', email_already_registered_msg.get_attribute("class"))
                cls.successful_non_complained_fields["@"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for '@'")
            print(" warn_e_under_breadcrumbs.text = ", warn_e_under_breadcrumbs.text)
            try:
                em_reg_before = cls.browser.find_element(By.XPATH, "//div[contains(., ' Warning: E-Mail Address is already registered!')]")
                print(" em_reg_before = ", em_reg_before)
                cls.successful_non_complained_fields["@"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for '@'")
            except NoSuchElementException:
                print(" element '//div[contains(.' not found")
            if str(warn_e_under_breadcrumbs.text).__contains__("rivacy") and \
                    str(warn_e_under_breadcrumbs.text).__contains__("olicy"): # privacy and policy

                print("/!\\ Privacy policy message alert Dismissible - present")
                cls.successful_non_complained_fields["V"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for 'V'")
                try:
                    cls.browser.find_element(By.XPATH, cls.all_els["V"]).click()
                except selenium.common.exceptions.ElementClickInterceptedException:
                    print("FAIL# Direct click by Xpath or Id - unavaiable. Click Intercepted. Workaround through js-script")
                    cls.browser.execute_script("arguments[0].click();", cls.browser.find_element(By.XPATH, cls.all_els["V"]))

            if (str(warn_e_under_breadcrumbs.text).__contains__("mail") or str(warn_e_under_breadcrumbs.text).__contains__("Mail")) and \
                    str(warn_e_under_breadcrumbs.text).__contains__("egistered"):

                print("/!\\ Existing e-mail account in system reg-attempt message alert Dismissible - present")
                cls.successful_non_complained_fields["@"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for '@'")
                if fix_tries_n == 2 or fix_tries_n < 0:
                    #uniquify field-value
                    new_val = cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value").replace("@", cls.digit_uniqificator("")+"@")
                if fix_tries_n == 1:
                    #length add-substract field-value
                    new_val1 = str(cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value")) + rstr.xeger(r"[a-zA-Z_]{1}")
                    new_val2 = re.sub("@.*[^.]{2,}.*", "@"+rstr.xeger(r"[a-zA-Z_]{1}")+str(".")+rstr.xeger(r"[a-zA-Z_]{1}"), str(cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value")))
                    new_val = random.choice([new_val1, new_val2])
                    cls.browser.find_element(By.XPATH, cls.all_els["@"]).clear()
                if fix_tries_n == 0:
                    #default field-value (has to guarantee to pass-through verification and leads to success registration even after previous fix-tries)
                    # adding extra rstr.xeger-chars as a stub where delete in DB of reliable e-mail supposed:
                    new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["@"])[0]).replace("@", cls.digit_uniqificator("") + "@" +rstr.xeger(r"[a-zA-Z0-9_]{8}"))
                if not provocation_coin_toss: cls.successful_non_complained_fields['@'] = new_val
                cls.browser.find_element(By.XPATH, cls.all_els["@"]).clear()
                cls.browser.find_element(By.XPATH, cls.all_els["@"]).send_keys(new_val)

        except selenium.common.exceptions.NoSuchElementException:
            print("No warn_e_under_breadcrumbs message on the page")
        ##############################################################
        warn_e_under_inp_fields = cls.browser.find_elements(By.CLASS_NAME, "text-danger")

        for warn_e_under_inp_field in warn_e_under_inp_fields:

            if str(warn_e_under_inp_field.text).__contains__("irst") and \
            str(warn_e_under_inp_field.text).__contains__("ame"):

                print("/!\\ First Name message alert - present")
                cls.successful_non_complained_fields["F"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for 'F'")
                if fix_tries_n == 2 or fix_tries_n < 0:
                    # uniquify field-value
                    if len(cls.browser.find_element(By.XPATH, cls.all_els["F"]).get_attribute("value")) > 1:
                        new_val = cls.replace_str_index(cls.browser.find_element(By.XPATH, cls.all_els["F"]).get_attribute("value"), 1, replacement=str(rstr.xeger(r"[a-zA-Z_]{1}")))
                    else:
                        new_val = cls.replace_str_index(cls.browser.find_element(By.XPATH, cls.all_els["F"]).get_attribute("value"), 0, replacement=str(rstr.xeger(r"[a-zA-Z_]{1}")))
                if fix_tries_n == 1:
                    # length add-substract field-value
                    new_val1 = str(cls.browser.find_element(By.XPATH, cls.all_els["F"]).get_attribute("value")) + rstr.xeger(r"[a-zA-Z_]{1}")
                    new_val2 = str(cls.browser.find_element(By.XPATH, cls.all_els["F"]).get_attribute("value"))[:len(str(cls.browser.find_element(By.XPATH, cls.all_els["F"]).get_attribute("value")))]
                    new_val = random.choice([new_val1, new_val2])
                    cls.browser.find_element(By.XPATH, cls.all_els["F"]).clear()
                if fix_tries_n == 0:
                    # default field-value (has to guarantee to pass-through verification and leads to success registration even after previous fix-tries)
                    new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["F"])[0])
                if not provocation_coin_toss: cls.successful_non_complained_fields['F'] = new_val
                cls.browser.find_element(By.XPATH, cls.all_els["F"]).clear()
                cls.browser.find_element(By.XPATH, cls.all_els["F"]).send_keys(new_val)

            if str(warn_e_under_inp_field.text).__contains__("ast") and \
            str(warn_e_under_inp_field.text).__contains__("ame"): # Last Name

                print("/!\\ Last Name message alert - present")
                cls.successful_non_complained_fields["L"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for 'L'")
                if fix_tries_n == 2 or fix_tries_n < 0:
                    # uniquify field-value
                    if len(cls.browser.find_element(By.XPATH, cls.all_els["L"]).get_attribute("value")) > 1:
                        new_val = cls.replace_str_index(cls.browser.find_element(By.XPATH, cls.all_els["L"]).get_attribute("value"), 1, replacement=str(rstr.xeger(r"[a-zA-Z_]{1}")))
                    else:
                        new_val = cls.replace_str_index(cls.browser.find_element(By.XPATH, cls.all_els["L"]).get_attribute("value"), 0, replacement=str(rstr.xeger(r"[a-zA-Z_]{1}")))
                if fix_tries_n == 1:
                    # length add-substract field-value
                    new_val1 = str(cls.browser.find_element(By.XPATH, cls.all_els["L"]).get_attribute("value")) + rstr.xeger(r"[a-zA-Z_]{1}")
                    new_val2 = str(cls.browser.find_element(By.XPATH, cls.all_els["L"]).get_attribute("value"))[:len(str(cls.browser.find_element(By.XPATH, cls.all_els["L"]).get_attribute("value")))]
                    new_val = random.choice([new_val1, new_val2])
                    cls.browser.find_element(By.XPATH, cls.all_els["L"]).clear()
                if fix_tries_n == 0:
                    # default field-value (has to guarantee to pass-through verification and leads to success registration even after previous fix-tries)
                    new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["L"])[0])
                if not provocation_coin_toss: cls.successful_non_complained_fields['L'] = new_val
                cls.browser.find_element(By.XPATH, cls.all_els["L"]).clear()
                cls.browser.find_element(By.XPATH, cls.all_els["L"]).send_keys(new_val)

            if str(warn_e_under_inp_field.text).__contains__("mail") or \
            str(warn_e_under_inp_field.text).__contains__("Mail"): # e-mail

                print("/!\\ E-Mail message alert - present")
                cls.successful_non_complained_fields["@"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for '@'")
                if fix_tries_n == 2 or fix_tries_n < 0:
                    # uniquify field-value
                    if cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value") is not None and cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value") != "": #23062023
                        new_val = cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value").replace("@", cls.digit_uniqificator("") + "@") #23062023
                    else: new_val = e_mail2.generate_email(limit=random.randint(3, 10)) #23062023
                if fix_tries_n == 1:
                    # length add-substract field-value
                    new_val1 = str(cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value")) + rstr.xeger(r"[a-zA-Z_]{1}")
                    new_val2 = re.sub("@.*[^.]{2,}.*", "@" + rstr.xeger(r"[a-zA-Z_]{1}") + str(".") + rstr.xeger(r"[a-zA-Z_]{1}"), str(cls.browser.find_element(By.XPATH, cls.all_els["@"]).get_attribute("value")))
                    new_val = random.choice([new_val1, new_val2])
                    cls.browser.find_element(By.XPATH, cls.all_els["@"]).clear()
                if fix_tries_n == 0:
                    # default field-value (has to guarantee to pass-through verification and leads to success registration even after previous fix-tries)
                    # adding extra rstr.xeger-chars as a stub where delete in DB of reliable e-mail supposed:
                    new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["@"])[0]).replace("@", cls.digit_uniqificator("") + "@" +rstr.xeger(r"[a-zA-Z0-9_]{8}"))
                print(f" new_val = {new_val}")
                if not provocation_coin_toss: cls.successful_non_complained_fields['@'] = new_val
                cls.browser.find_element(By.XPATH, cls.all_els["@"]).clear()
                cls.browser.find_element(By.XPATH, cls.all_els["@"]).send_keys(new_val)

            if str(warn_e_under_inp_field.text).__contains__("elephone"): # Telephone number

                print("/!\\ Telephone number message alert - present")
                cls.successful_non_complained_fields["#"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for '#'")
                if fix_tries_n == 2 or fix_tries_n < 0:
                    # uniquify field-value
                    new_val = cls.replace_str_index(cls.browser.find_element(By.XPATH, cls.all_els["#"]).get_attribute("value"), 1, cls.digit_uniqificator(""))
                if fix_tries_n == 1:
                    # length add-substract field-value
                    new_val1 = str(cls.browser.find_element(By.XPATH, cls.all_els["#"]).get_attribute("value")) + rstr.xeger(r"[0-9]{1}")
                    new_val2 = re.sub("[0-9].*$", "", str(cls.browser.find_element(By.XPATH, cls.all_els["#"]).get_attribute("value")))
                    new_val = random.choice([new_val1, new_val2])
                    cls.browser.find_element(By.XPATH, cls.all_els["#"]).clear()
                if fix_tries_n == 0:
                    # default field-value (has to guarantee to pass-through verification and leads to success registration even after previous fix-tries)
                    new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["#"])[0])
                if not provocation_coin_toss: cls.successful_non_complained_fields['#'] = new_val
                cls.browser.find_element(By.XPATH, cls.all_els["#"]).clear()
                cls.browser.find_element(By.XPATH, cls.all_els["#"]).send_keys(new_val)

            if not str(warn_e_under_inp_field.text).__contains__("onfirm") and \
                    str(warn_e_under_inp_field.text).__contains__("ssword"): # 1st password input

                print("/!\\ 1 password message alert - present")
                cls.successful_non_complained_fields["p"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for 'p'")
                if fix_tries_n == 2 or fix_tries_n < 0:
                    # uniquify field-value
                    new_val = cls.replace_str_index(cls.browser.find_element(By.XPATH, cls.all_els["p"]).get_attribute("value"), 1, cls.digit_uniqificator(""))
                if fix_tries_n == 1:
                    # length add-substract field-value
                    new_val1 = str(cls.browser.find_element(By.XPATH, cls.all_els["p"]).get_attribute("value")) + rstr.xeger(r"[0-9]{1}")
                    new_val2 = re.sub("[0-9].*$", "", str(cls.browser.find_element(By.XPATH, cls.all_els["p"]).get_attribute("value")))
                    new_val = random.choice([new_val1, new_val2])
                    cls.browser.find_element(By.XPATH, cls.all_els["p"]).clear()
                if fix_tries_n == 0:
                    # default field-value (has to guarantee to pass-through verification and leads to success registration even after previous fix-tries)
                    new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["p"])[0])
                if not provocation_coin_toss: cls.successful_non_complained_fields['p'] = new_val
                cls.browser.find_element(By.XPATH, cls.all_els["p"]).clear()
                cls.browser.find_element(By.XPATH, cls.all_els["p"]).send_keys(new_val)

            if str(warn_e_under_inp_field.text).__contains__("onfirm") and \
            str(warn_e_under_inp_field.text).__contains__("ssword"): # Password confirmation

                print("/!\\ 2 password confirm message alert - present")
                cls.successful_non_complained_fields["d"] = "complained" # placeholder for further test-development for given situation
                print("'complained' value set for 'd'")
                if fix_tries_n == 2 or fix_tries_n < 0:
                    new_val = cls.browser.find_element(By.XPATH, cls.all_els["p"]).get_attribute("value")

                if fix_tries_n == 1:
                    try:
                        new_val = cls.generated_assimilated_strs_dict_to_mas_forwarding_cls["p"]
                    except KeyError:
                        new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["d"])[0])

                if fix_tries_n == 0:
                    # default field-value (has to guarantee to pass-through verification and leads to success registration even after previous fix-tries)
                    new_val = str(list(cls.generated_assimilated_strs_dict_to_mas_forwarding_stub_cls["d"])[0])
                if not provocation_coin_toss: cls.successful_non_complained_fields['d'] = new_val
                cls.browser.find_element(By.XPATH, cls.all_els["d"]).clear()
                cls.browser.find_element(By.XPATH, cls.all_els["d"]).send_keys(new_val)
        print(f">>>>>>>>>>>>>>>>>>>cls.successful_non_complained_fields = {cls.successful_non_complained_fields}")
