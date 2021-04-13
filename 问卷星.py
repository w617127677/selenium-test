from selenium import webdriver
import random
import time 
# for p in range(1,10):
    
# driver.find_element_by_xpath('//ul[1]/li[2]/a').click()
# for i in range(1,10):
l=0


while True:

# try:
    # options = webdriver.ChromeOptions()
    # chrome_prefs = {}
    # options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}
    # chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)


    driver = webdriver.Chrome()
    driver.get('https://www.wjx.cn/jq/88870298.aspx')
    # time.sleep(0.1)
    a=random.randint(2,4)
    driver.find_element_by_xpath(f'//div[@id="divquestion1"]//ul/li[{a}]/a').click()
    b=random.randint(1,2)


    driver.find_element_by_xpath(f'//div[@id="divquestion2"]//ul/li[{b}]/a').click()
    c=random.randint(1,5)
    driver.find_element_by_xpath(f'//div[@id="divquestion3"]//ul/li[{c}]/a').click()
    driver.find_element_by_xpath(f'//div[@id="divquestion4"]//ul/li[{random.randint(1,5)}]/a').click()
    driver.find_element_by_xpath(f'//div[@id="divquestion5"]//ul/li[{random.randint(1,5)}]/a').click()
    driver.find_element_by_xpath(f'//div[@id="divquestion6"]//ul/li[{random.randint(1,5)}]/a').click()
    # for q in range(random.randint(1,7)):
    e=random.randint(1,4)
    f=random.randint(5,7)
    # for q in range(3):
    driver.find_element_by_xpath(f'//div[@id="divquestion7"]//ul/li[{e}]/a').click()
    driver.find_element_by_xpath(f'//div[@id="divquestion7"]//ul/li[{f}]/a').click()
    #     for q in range(4):

    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div8']/div[@id='divquestion8']/table/tbody/tr[1]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div8']/div[@id='divquestion8']/table/tbody/tr[2]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div8']/div[@id='divquestion8']/table/tbody/tr[3]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div9']/div[@id='divquestion9']/table/tbody/tr[1]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div9']/div[@id='divquestion9']/table/tbody/tr[2]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div9']/div[@id='divquestion9']/table/tbody/tr[3]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div10']/div[@id='divquestion10']/table/tbody/tr[1]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div10']/div[@id='divquestion10']/table/tbody/tr[2]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div10']/div[@id='divquestion10']/table/tbody/tr[3]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div11']/div[@id='divquestion11']/table/tbody/tr[1]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div11']/div[@id='divquestion11']/table/tbody/tr[2]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div11']/div[@id='divquestion11']/table/tbody/tr[3]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div12']/div[@id='divquestion12']/table/tbody/tr[1]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div12']/div[@id='divquestion12']/table/tbody/tr[2]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div12']/div[@id='divquestion12']/table/tbody/tr[3]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div13']/div[@id='divquestion13']/table/tbody/tr[1]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div13']/div[@id='divquestion13']/table/tbody/tr[2]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div13']/div[@id='divquestion13']/table/tbody/tr[3]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div14']/div[@id='divquestion14']/table/tbody/tr[1]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div14']/div[@id='divquestion14']/table/tbody/tr[2]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div14']/div[@id='divquestion14']/table/tbody/tr[3]/td[{}]/a".format(random.randint(1,5))).click()
    driver.find_element_by_id('submit_button').click()
    try:
        driver.find_element_by_id('rectBottom').click()
    except:
        pass
    # driver.close()
    l=l+1
    print(l,'yes')
# except:
#     print('no')
    # driver.quit()





# driver.find_element_by_xpath(f'//div[@id="divquestion7"]//ul/li[{f}]/a').click()
    # driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div2']/div[@id='divquestion2']/ul[@class='ulradiocheck']/li[1]/a").click()
    # driver.find_element_by_xpath("/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div3']/div[@id='divquestion3']/ul[@class='ulradiocheck']/li[1]/a").click()
    # driver.find_element_by_id('submit_button').click()
    # driver.delete_all_cookies()
    # driver.close()
    # driver.quit()
    
    # time.sleep(180)