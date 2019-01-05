from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time

driver = webdriver.Chrome('/Users/Максим/Desktop/chromedriver')

data=['accounts_payable','accum_depre','assets','assets_curr','assets_curr_oth','bookvalue_ps','capex','cash',
'cash_st','cashflow_fin','cashflow_invst','cashflow_op','cogs','cost_of_revenue','current_ratio','debt',
'debt_lt','debt_lt_curr','debt_st','depre','depre_amort','EBIT','EBITDA','eps','equity','goodwill','income','income_beforeextra','income_tax','income_tax_payable','interest_expense',
'inventory','inventory_turnover','liabilities','liabilities_cur_oth','liabilities_curr','liabilities_oth',
'operating_expense','operating_income','operating_margin','ppent','ppent_net','preferred_dividends',
'pretax_income','quick_ratio','receivable','retained_earnings','return_assets','return_equity','revenue',
'sales','SGA_expense','1']
l=len(data)
neu=['none','market','industry','subindustry']
start = time.time()
def login():
    driver.get("https://websim.worldquantchallenge.com/en/cms/wqc/websim/")
    driver.implicitly_wait(10)
    login = driver.find_element_by_name("EmailAddress")
    login.send_keys("login")###логин
    driver.implicitly_wait(10)
    password=driver.find_element_by_name("Password")
    password.send_keys("password")###пароль
    driver.implicitly_wait(10)
    button=driver.find_element_by_xpath("/html/body/main/article/section/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div[4]/span[1]/button")
    time.sleep(0.5)
    button.click()
def click():
    button = driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[2]/div/div/div[2]/button')
    try:
            button.click()
    except WebDriverException:
            field.send_keys(Keys.ESCAPE)
            button.click()
    try:
            driver.implicitly_wait(250)
            result = driver.find_element_by_id("resultTabPanel")
    except NoSuchElementException:
            out=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[2]/div/div/div/div[3]/div/a")
            out.click()
            driver.implicitly_wait(30)
            button1 = driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[2]/div/div/div[2]/button')
            button1.click()
            try:
                driver.implicitly_wait(250)
                result = driver.find_element_by_id("resultTabPanel")
            except NoSuchElementException:
                print('fuck')
                
start=time.time()
def perebor(a,b,c,d,e,f,data):
    for k in range(a,b):
        for i in range(c,d):
            for j in range(e,f):
                driver.get("https://websim.worldquantchallenge.com/simulate")
                driver.implicitly_wait(60)
                button1=driver.find_element_by_xpath('/html/body/main/article/div/div/div[1]/div/div[1]/div/div[1]/button[1]')
                button1.click()
                button2=driver.find_element_by_xpath('/html/body/main/article/div/div/div[1]/div/div[1]/div/div[2]/div/section/section[1]/form/div/div[6]/div/div/select')
                button2.send_keys(neu[k])
                time.sleep(2)
                button1.click()
                time.sleep(1)
                driver.implicitly_wait(30)
                invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
                invite.click()
                field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
                field.send_keys("rank(" + data[i]+"/"+data[j]+")")
                field.send_keys(Keys.SHIFT,Keys.ENTER)
                time.sleep(2)
                field.send_keys(Keys.ESCAPE)
                driver.implicitly_wait(5)
                click()
                driver.implicitly_wait(250)
                result = driver.find_element_by_id("resultTabPanel")
                time.sleep(2)
                driver.implicitly_wait(60)
                stats=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
                stats.click()
                time.sleep(2)
                driver.implicitly_wait(100)
                sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[12]/td[4]/span')
                fitness=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[12]/td[5]/span')
                print(neu[k]+" "+sharpe.text+" "+fitness.text+" rank(" + data[i]+"/"+data[j]+")")

login()
time.sleep(5)
perebor(1,4,0,1,41,l,data)
