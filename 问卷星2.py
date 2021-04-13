# coding=utf-8
from selenium import webdriver
import random
import time



while True:

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--headless")
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'

        )
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)
        with open('stealth.min.js', encoding='utf-8') as f:

            js = f.read()

        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js,

        })
        driver.get('https://www.wjx.cn/vj/eTU21ro.aspx')
        time.sleep(0.5)
        driver.find_element_by_xpath(f'//div[@id="divquestion1"]//ul/li[{random.randint(1, 4)}]/a').click()
        time.sleep(1)
        driver.find_element_by_id('submit_button').click()
        driver.close()
        time.sleep(1)

        print('成功')

    except:
        print('失败')
# while True:
#
#     try:
#         # options = webdriver.ChromeOptions()
#         # # chrome_prefs = {}
#         # # options.experimental_options["prefs"] = chrome_prefs
#         # # chrome_prefs["profile.default_content_settings"] = {"images": 2}
#         # # chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
#         # options.add_argument('--headless')
#         # driver = webdriver.Chrome(options=options)
#         driver = webdriver.Chrome()
#
#         # driver = webdriver.Chrome()
#         driver.get('https://www.wjx.cn/vj/PAFhGa0.aspx')
#         # time.sleep(0.1)
#         a = random.randint(1, 4)
#         driver.find_element_by_xpath(f'//div[@id="divquestion1"]//ul/li[{a}]/a').click()
#         b = random.randint(1, 2)
#
#         driver.find_element_by_xpath(f'//div[@id="divquestion2"]//ul/li[{b}]/a').click()
#         c = random.randint(1, 5)
#         driver.find_element_by_xpath(f'//div[@id="divquestion3"]//ul/li[{c}]/a').click()
#         driver.find_element_by_xpath(f'//div[@id="divquestion4"]//ul/li[{random.randint(1, 5)}]/a').click()
#         driver.find_element_by_xpath(f'//div[@id="divquestion5"]//ul/li[{random.randint(1, 5)}]/a').click()
#         driver.find_element_by_xpath(f'//div[@id="divquestion6"]//ul/li[{random.randint(1, 5)}]/a').click()
#         # for q in range(random.randint(1,7)):
#         e = random.randint(1, 4)
#         f = random.randint(5, 7)
#         # for q in range(3):
#         driver.find_element_by_xpath(f'//div[@id="divquestion7"]//ul/li[{e}]/a').click()
#         driver.find_element_by_xpath(f'//div[@id="divquestion7"]//ul/li[{f}]/a').click()
#         #     for q in range(4):
#
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div8']/div[@id='divquestion8']/table/tbody/tr[1]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div8']/div[@id='divquestion8']/table/tbody/tr[2]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div8']/div[@id='divquestion8']/table/tbody/tr[3]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div9']/div[@id='divquestion9']/table/tbody/tr[1]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div9']/div[@id='divquestion9']/table/tbody/tr[2]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div9']/div[@id='divquestion9']/table/tbody/tr[3]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div10']/div[@id='divquestion10']/table/tbody/tr[1]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div10']/div[@id='divquestion10']/table/tbody/tr[2]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div10']/div[@id='divquestion10']/table/tbody/tr[3]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div11']/div[@id='divquestion11']/table/tbody/tr[1]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div11']/div[@id='divquestion11']/table/tbody/tr[2]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div11']/div[@id='divquestion11']/table/tbody/tr[3]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div12']/div[@id='divquestion12']/table/tbody/tr[1]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div12']/div[@id='divquestion12']/table/tbody/tr[2]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div12']/div[@id='divquestion12']/table/tbody/tr[3]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div13']/div[@id='divquestion13']/table/tbody/tr[1]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div13']/div[@id='divquestion13']/table/tbody/tr[2]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div13']/div[@id='divquestion13']/table/tbody/tr[3]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div14']/div[@id='divquestion14']/table/tbody/tr[1]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div14']/div[@id='divquestion14']/table/tbody/tr[2]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_xpath(
#             "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div14']/div[@id='divquestion14']/table/tbody/tr[3]/td[{}]/a".format(
#                 random.randint(1, 5))).click()
#         driver.find_element_by_id('submit_button').click()
#         driver.close()
#         l=l+1
#         print(l,'yes')
#     except:
#         print('no')
    # driver.quit()

# driver.find_element_by_xpath(f'//div[@id="divquestion7"]//ul/li[{f}]/a').click()
# driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div2']/div[@id='divquestion2']/ul[@class='ulradiocheck']/li[1]/a").click()
# driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div3']/div[@id='divquestion3']/ul[@class='ulradiocheck']/li[1]/a").click()
# driver.find_element_by_id('submit_button').click()
# driver.delete_all_cookies()
# driver.close()
# driver.quit()

# time.sleep(180)