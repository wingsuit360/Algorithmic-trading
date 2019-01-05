from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time

driver = webdriver.Chrome('/Users/Максим/Desktop/chromedriver')
start = time.time()
def login():
    driver.get("https://websim.worldquantchallenge.com/en/cms/wqc/websim/")
    driver.implicitly_wait(10)
    login = driver.find_element_by_name("EmailAddress")
    login.send_keys("login")
    driver.implicitly_wait(10)
    password=driver.find_element_by_name("Password")
    password.send_keys("password")
    driver.implicitly_wait(10)
    button=driver.find_element_by_xpath("/html/body/main/article/section/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div[4]/span[1]/button")
    time.sleep(0.5)
    button.click()
login()
time.sleep(1)
start=time.time()
neu=['none','market','industry','subindustry']
l_neu=len(neu)
######  market usa top200 pool0    ######
######alphas = ['delta(working_capital,196)','delta(sga_expense,172) ','delta(delta(-delta(rank(capex),46),49),51)','delta(-delta(rank(capex),46),51) ','decay_exp(-delta(rank(capex),46),1,50) ','rank(delta(cash,76))','ts_min(ts_rank((assets_curr+5)/(inventory+50),256),50) ','rank(delta(assets_curr,250)/floor(decay_linear(income_tax,50)))','rank(decay_linear(floor(assets_curr),2)/floor(decay_linear(income_tax,50))) ','ts_min(rank(decay_linear(floor(assets_curr),2)/floor(decay_linear(income_tax,50))),50)']
######  market usa top200 pool1   #######
######alphas = ['round(decay_linear(ts_max(ts_rank(assets_curr/invested_capital,256),40),50))','decay_linear(ts_max(ts_rank(assets_curr/invested_capital,256),40),50)','indneutralize(rank(decay_exp(((assets_curr+80)/(cashflow_op-750)),0.01,50)),industry)','arcsin(ts_rank(ts_max((assets_curr-350)/(debt-50),65),256))','indneutralize((ts_rank(ts_max((assets_curr-350)/(debt-50),65),256)),subindustry)','log(1+ts_rank(decay_exp(ts_max((assets_curr-150)/debt_lt,38),0.1,50),256))','delta(ts_rank(sum(assets_curr,32)/ts_min(cashflow_op-100,100),256),57)','arcsin(ts_rank(sum(assets_curr,32)/ts_min(cashflow_op-100,100),256))','-ts_rank(assets_curr/cashflow_invst,256)','decay_exp(ts_rank((decay_exp(assets_curr+150,0.001,30)/(capex-52)),256),1,50)']
######   market usa top200 pool2   ######
######alphas =['ts_rank(decay_exp(assets_curr+250,0.1,50)/bookvalue_ps,256)','(ts_max(decay_linear(rank((assets_curr-250)/(ebit+130)),40),3))','ts_max(decay_linear(rank(assets_curr/ebit),30),3)','ts_min(decay_exp(fraction(rank(ts_max(assets_curr-50,2)/(debt-100))),1,350),150)','decay_exp(fraction(rank(ts_max(assets_curr-50,2)/(debt-0.1))),1,350)','delta((rank(eps)),120)','(decay_exp(-rank((assets+50)/cashflow_invst),1,50)) ','scale(delay(ts_max(humpdecay(decay_exp(rank(assets/debt_lt),1,50),0.01),90),30)) ','round(ts_min(decay_exp(argmin(rank((assets)/debt_lt),50),0.1,10),50)) ','decay_exp(rank(sum(assets,30)/ts_min(income_tax,7)),1,150)']
######    market usa top200 пул3   #######
######alphas = ['delta(delta(-rank((capex)/assets),290),150)','delta(-rank((capex)/assets),290)','delta(-rank((capex)/assets),151)','delta(delta(-rank((capex)/assets),60),364)','delta(delta(-rank((capex)/assets),60),321)','delta(-ts_rank(bookvalue_ps/ebit,256),72)','delta(-ts_rank(bookvalue_ps/ebit,256),88)','delta(-ts_rank(bookvalue_ps/ebit,256),100)','delta(-ts_rank(bookvalue_ps/ebit,256),118)','delta(-ts_rank(bookvalue_ps/ebit,256),136)']
######    market usa top200 pool4  ####
######alphas = ['delta(rank(assets_curr),162)','delta(rank(assets_curr),182)','delta(-rank((capex)/cogs),338)','delta(log(-1/(-rank(sum(capex,50)/cashflow_dividends))),301)','delta(-rank(capex/cashflow_dividends),245)','delta(-ts_rank(capex/cash,256),251)','delta(-ts_rank(capex/assets_curr,256),252)','delta(delta(-rank(capex/cash),321),151)','delta(-rank(capex/cash),179)','delta(delta(-rank(capex/cash),179),256)']
######    market usa top200 pool5   #####
######alphas = ['delta(rank((sum(operating_income-50,50))/sum(depre_amort,50)),149) ','delta(delta(rank((sum(operating_income-50,50))/sum(depre_amort,50)),90),150) ','delta(floor(arcsin(-ts_rank(capex/(inventory_turnover+70),256))),250)','arcsin(-ts_rank(delta(capex,207)/decay_exp(inventory_turnover+70,0.1,50),256))','arcsin(-ts_rank(capex/floor(decay_exp(inventory_turnover+70,0.1,50)),256))','arcsin(-ts_rank(capex/fraction(decay_exp(inventory_turnover+70,0.1,50)),256))','arcsin(-ts_rank(capex/ceiling(decay_exp(inventory_turnover+70,0.1,50)),256))','floor(arcsin(-ts_rank(capex/(inventory_turnover+70),256)))','delta(-ts_rank(capex/(inventory_turnover+70),256),173)','indneutralize(arcsin(-ts_rank(capex/(inventory_turnover+70),256)),industry)']
######    industry usa top200 pool0   ######
######alphas = ['indneutralize(decay_linear(ts_min(rank(fraction(assets_curr)/retained_earnings),50),50),industry)','-ts_rank(bookvalue_ps/ebit,256) ','delta(-ts_rank(bookvalue_ps/ebit,256),119)','delta(-ts_rank(bookvalue_ps/ebit,256),160)','decay_exp(-ts_rank(bookvalue_ps/ebit,256),1,50) ','(-1/ts_min(rank(assets_curr/income_tax),40))','delta((-1/ts_min(rank(assets_curr/income_tax),40)),73)','delta((-1/ts_min(rank(assets_curr/income_tax),40)),191)','delta((-1/ts_min(rank(assets_curr/income_tax),40)),460)','indneutralize(decay_linear(ts_min(rank(decay_linear((assets_curr-150),50)/retained_earnings),50),50),industry)']
######    industry usa top200 pool1   ########
######alphas = ['delta(-ts_rank(ts_min(capex,50)/ts_max(revenue,50),256),150)','-ts_rank(ts_min(capex,50)/ts_max(revenue,50),256)','delta(delta(rank(bookvalue_ps/pretax_income),209),171)','delta(delta(rank(bookvalue_ps/pretax_income),209),200)','delta(rank(bookvalue_ps/pretax_income),209)','-ts_rank((bookvalue_ps-50)/sales_growth,156)','-rank(decay_linear(bookvalue_ps-50,50)/decay_linear(retained_earnings,40))','-rank(decay_linear(bookvalue_ps-50,50)/retained_earnings)','-ts_rank(bookvalue_ps/ebitda,256)','delta(-ts_rank(bookvalue_ps/ebit,256),138)']
######    subindustry usa top200 pool0 ########
######alphas = ['indneutralize(ts_min(-rank((bookvalue_ps-150)/income_tax),38),1)','delta(ts_min(-rank((bookvalue_ps-150)/income_tax),38),80)','delta(ts_min(-rank((bookvalue_ps-150)/income_tax),38),200)','rank(floor(bookvalue_ps)/debt_lt)','fraction(rank(ts_min(bookvalue_ps,40)/floor(debt_lt)))','decay_exp(fraction(rank(ts_min(bookvalue_ps,40)/floor(debt_lt))),0.1,50)','delta(-ts_rank(bookvalue_ps/cash,256),200)','decay_exp(-ts_rank(bookvalue_ps/cash,256),1,50)','delta(-ts_rank(bookvalue_ps/cash,256),58)','delta(-ts_rank(bookvalue_ps/cash,256),250)']
######    subindustry usa top200 pool1 #######
######alphas = ['rank(-1/(ts_max(rank(rank(decay_exp(capex-160,1,70)/decay_linear(rd_expense,70))),75)))','indneutralize(rank(decay_linear(capex,2)/ts_max(debt-50,60)),subindustry)','rank(decay_linear(capex,2)/ts_max(debt-50,60))','rank(log(capex+1)/ts_max(debt-50,60))','rank(capex/ts_max(debt-50,60))','delta(-ts_rank(bookvalue_ps/retained_earnings,256),109)','delta(delta(ts_min(-rank((bookvalue_ps-150)/income_tax),38),200),100)','delta(delta(ts_min(-rank((bookvalue_ps-150)/income_tax),38),162),100)','delta(delta(ts_min(-rank((bookvalue_ps-150)/income_tax),38),80),250)','delta(ts_min(-rank((bookvalue_ps-150)/income_tax),38),162)']
######   subind usa top200 pool2   #######
alphas = ['ts_max(rank(rank(decay_exp(capex-160,1,70)/decay_linear(rd_expense,70))),70)','rank(rank(decay_exp(capex-160,1,70)/decay_linear(rd_expense,70)))','delta(delta(-rank(decay_exp(capex-100,1,50)/ts_min(ebit-20,50)),51),89)','delta(delta(-rank(decay_exp(capex-100,1,50)/ts_min(ebit-20,50)),51),47)','delta(-rank(decay_exp(capex-100,1,50)/ts_min(ebit-20,50)),57)','-rank(decay_exp(capex-100,1,50)/ts_min(ebit-20,50))','indneutralize(rank(decay_linear(capex,2)/ts_max(debt-50,60)),subindustry)','rank(decay_linear(capex,2)/ts_max(debt-50,60))','rank(log(capex+1)/ts_max(debt-50,60))','rank(capex/ts_max(debt-50,60))']




l_alphas=len(alphas)
string = ['fraction(-ts_rank(capex/sales_ps,256))','delta(-ts_rank(capex/sales_ps,256),250)','']
l_string=len(string)

def click():
    button = driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[2]/div/div/div[2]/button')
    try:
            button.click()
    except WebDriverException:
            field.send_keys(Keys.ESCAPE)
            button.click()
    try:
            driver.implicitly_wait(180)
            result = driver.find_element_by_id("resultTabPanel")
    except NoSuchElementException:
            out=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[2]/div/div/div/div[3]/div/a")
            out.click()
            driver.implicitly_wait(15)
            button1 = driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[2]/div/div/div[2]/button')
            button1.click()
            try:
                driver.implicitly_wait(180)
                result = driver.find_element_by_id("resultTabPanel")
            except NoSuchElementException:
                print('fuck')


for i in range (1,3):
    for k in range (0,l_string):
        for j in range (0,l_alphas):#####потом 6 и 1 на сабиндастри
            #now = time.time()
            #if (now-start)>2700:
             #   driver.get('https://websim.worldquantchallenge.com/logout')
             #   time.sleep(1)
             #   login()
              #  time.sleep(1)
              #  try:
               #     login()
               #     start=time.time()
                #except NoSuchElementException:
                #    start=time.time()
            #time.sleep(0.2)
            driver.get("https://websim.worldquantchallenge.com/simulate")
            driver.implicitly_wait(30)
            button1=driver.find_element_by_xpath('/html/body/main/article/div/div/div[1]/div/div[1]/div/div[1]/button[1]')
            button1.click()
            button2=driver.find_element_by_xpath('/html/body/main/article/div/div/div[1]/div/div[1]/div/div[2]/div/section/section[1]/form/div/div[6]/div/div/select')
            button2.send_keys(neu[i])
            time.sleep(2)
            button1.click()
            time.sleep(1)
            driver.implicitly_wait(30)
            invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
            invite.click()
            field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
            field.send_keys('x1 = '+string[k]+';')
            field.send_keys(Keys.SHIFT,Keys.ENTER)
            field.send_keys(Keys.ESCAPE)
            field.send_keys('x2 = '+alphas[j]+';')
            field.send_keys(Keys.SHIFT,Keys.ENTER)
            field.send_keys(Keys.ESCAPE)
            field.send_keys('y1 = scale(x1) + scale(x2);')
            field.send_keys(Keys.SHIFT,Keys.ENTER)
            field.send_keys(Keys.ESCAPE)
            field.send_keys('z1 = indneutralize(y1,1);')
            field.send_keys(Keys.SHIFT,Keys.ENTER)
            field.send_keys(Keys.ESCAPE)
            field.send_keys('z1==z1? z1 : groupmean(z1, market,0.01)')
            field.send_keys(Keys.SHIFT,Keys.ENTER)
            field.send_keys(Keys.ESCAPE)
            driver.implicitly_wait(5)
            click()
            driver.implicitly_wait(180)
            result = driver.find_element_by_id("resultTabPanel")
            time.sleep(2)
            driver.implicitly_wait(30)
            stats=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
            stats.click()
            time.sleep(2)
            driver.implicitly_wait(100)
            sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
            fitness=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[5]/span')
            print(sharpe.text)
            print(fitness.text)
            time.sleep(2)
            if float(sharpe.text)>=1.25 and float(fitness.text)>=1.01:
                submit=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/a[4]')
                submit.click()
                driver.implicitly_wait(30)
                submit_click=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/button')
                submit_click.click()
            print(neu[i]+' '+string[k]+' '+alphas[j])
