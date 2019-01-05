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
    proverka = input()
    if proverka == 'y':
        driver.implicitly_wait(10)
        button=driver.find_element_by_xpath("/html/body/main/article/section/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div[4]/span[1]/button")
        time.sleep(0.5)
        button.click() 
login()
time.sleep(1)
start=time.time()
currentstring='rank(capex/receivable)'#### строка для перебора
operatorsts =['sum','ts_max','ts_median','ts_min','decay_linear','arcsin','log','ceiling','fraction','round']####набор операторов
operatorstsall_n =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
l = len(operatorsts)

##################################    все выражение    ##############################





def ts_m(currentstring):                         
    for i in range (0,2):
    
        driver.get("https://websim.worldquantchallenge.com/simulate")
        driver.implicitly_wait(30)
        invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
        invite.click()
        field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
        field.send_keys(operatorsts[i]+'('+currentstring+',50)')
        field.send_keys(Keys.SHIFT,Keys.ENTER)
        field.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(5)
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
        driver.implicitly_wait(180)
        result = driver.find_element_by_id("resultTabPanel")
        driver.implicitly_wait(10)
        sharpe=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
        sharpe.click()
        driver.implicitly_wait(5)
        ooo=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr/td[7]')
        ooo_text=ooo.text
        if ooo_text.find('0')==0:
            print(operatorsts[i],'лажа полная,все по 0')
        else:
            sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
            operatorstsall_n[i+1]=float(sharpe.text)
            print(operatorsts[i],operatorstsall_n[i+1])

    for i in range (5,7):
    
        driver.get("https://websim.worldquantchallenge.com/simulate")
        driver.implicitly_wait(30)
        invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
        invite.click()
        field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
        field.send_keys(operatorsts[i]+'('+currentstring+')')
        field.send_keys(Keys.SHIFT,Keys.ENTER)
        field.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(5)
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
        driver.implicitly_wait(180)
        result = driver.find_element_by_id("resultTabPanel")
        driver.implicitly_wait(10)
        sharpe=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
        sharpe.click()
        driver.implicitly_wait(5)
        ooo=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr/td[7]')
        ooo_text=ooo.text
        if ooo_text.find('0')==0:
            print(operatorsts[i],'лажа полная,все по 0')
        else:
            sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
            operatorstsall_n[i+1]=float(sharpe.text)
            print(operatorsts[i],operatorstsall_n[i+1])
            
    if operatorstsall_n.index(max(operatorstsall_n)) == 0:
        currentstring=currentstring
    elif operatorstsall_n.index(max(operatorstsall_n))>5:
        currentstring = operatorsts[operatorstsall_n.index(max(operatorstsall_n))-1]+'('+currentstring+') '
    else:currentstring = operatorsts[operatorstsall_n.index(max(operatorstsall_n))-1]+'('+currentstring+',50)'

    return currentstring


#######################        знаменатель       #########################




def ts_1(currentstring):                         
    for i in range (0,2):
        currentstring_11=currentstring[currentstring.find('/')+1:currentstring.rfind(')')]
        currentstring_10=currentstring[:currentstring.find('/')]   
        driver.get("https://websim.worldquantchallenge.com/simulate")
        driver.implicitly_wait(30)
        invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
        invite.click()
        field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
        field.send_keys(currentstring_10+'/'+operatorsts[i]+'('+currentstring_11+',50))')
        field.send_keys(Keys.SHIFT,Keys.ENTER)
        field.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(5)
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
        driver.implicitly_wait(180)
        result = driver.find_element_by_id("resultTabPanel")
        driver.implicitly_wait(10)
        sharpe=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
        sharpe.click()
        driver.implicitly_wait(5)
        ooo=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr/td[7]')
        ooo_text=ooo.text
        if ooo_text.find('0')==0:
            print(operatorsts[i],'лажа полная,все по 0')
        else:
            sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
            operatorstsall_n[i+1]=float(sharpe.text)
            print(operatorsts[i],operatorstsall_n[i+1])
            
    for i in range (5,7):
    
        driver.get("https://websim.worldquantchallenge.com/simulate")
        driver.implicitly_wait(30)
        invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
        invite.click()
        field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
        field.send_keys(currentstring_10+'/'+operatorsts[i]+'('+currentstring_11+'))')
        field.send_keys(Keys.SHIFT,Keys.ENTER)
        field.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(5)
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
        driver.implicitly_wait(180)
        result = driver.find_element_by_id("resultTabPanel")
        driver.implicitly_wait(10)
        sharpe=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
        sharpe.click()
        driver.implicitly_wait(5)
        ooo=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr/td[7]')
        ooo_text=ooo.text
        if ooo_text.find('0')==0:
            print(operatorsts[i],'лажа полная,все по 0')
        else:
            sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
            operatorstsall_n[i+1]=float(sharpe.text)
            print(operatorsts[i],operatorstsall_n[i+1])
            

    if operatorstsall_n.index(max(operatorstsall_n)) == 0:
        currentstring=currentstring
    elif operatorstsall_n.index(max(operatorstsall_n))>5:
        currentstring = currentstring_10+'/'+operatorsts[operatorstsall_n.index(max(operatorstsall_n))-1]+'('+currentstring_11+'))'
    else:currentstring = currentstring_10+'/'+operatorsts[operatorstsall_n.index(max(operatorstsall_n))-1]+'('+currentstring_11+',50))'

    return currentstring


##########################     числитель      #####################


currentstring_10=currentstring[currentstring.find('/')+1:]
def ts_2(currentstring):                         
    for i in range (0,2):
        currentstring_11=currentstring[currentstring.find('(')+1:currentstring.rfind('/')]
        currentstring_10=currentstring[currentstring.find('/')+1:]
        driver.get("https://websim.worldquantchallenge.com/simulate")
        driver.implicitly_wait(30)
        invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
        invite.click()
        field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
        field.send_keys('rank('+operatorsts[i]+'('+currentstring_11+',50)/'+currentstring_10)
        field.send_keys(Keys.SHIFT,Keys.ENTER)
        field.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(5)
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
        driver.implicitly_wait(180)
        result = driver.find_element_by_id("resultTabPanel")
        driver.implicitly_wait(10)
        sharpe=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
        sharpe.click()
        driver.implicitly_wait(5)
        ooo=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr/td[7]')
        ooo_text=ooo.text
        if ooo_text.find('0')==0:
            print(operatorsts[i],'лажа полная,все по 0')
        else:
            sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
            operatorstsall_n[i+1]=float(sharpe.text)
            print(operatorsts[i],operatorstsall_n[i+1])
            
    for i in range (5,7):
    
        driver.get("https://websim.worldquantchallenge.com/simulate")
        driver.implicitly_wait(30)
        invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
        invite.click()
        field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
        field.send_keys('rank('+operatorsts[i]+'('+currentstring_11+')/'+currentstring_10)
        field.send_keys(Keys.SHIFT,Keys.ENTER)
        field.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(5)
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
        driver.implicitly_wait(180)
        result = driver.find_element_by_id("resultTabPanel")
        driver.implicitly_wait(10)
        sharpe=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
        sharpe.click()
        driver.implicitly_wait(10)
        ooo=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr/td[7]')
        ooo_text=ooo.text
        if ooo_text.find('0')==0:
            print(operatorsts[i],'лажа полная,все по 0')
        else:
            sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
            operatorstsall_n[i+1]=float(sharpe.text)
            print(operatorsts[i],operatorstsall_n[i+1])
            

    if operatorstsall_n.index(max(operatorstsall_n)) == 0:
        currentstring=currentstring
    elif operatorstsall_n.index(max(operatorstsall_n))>5:
        currentstring = 'rank('+operatorsts[operatorstsall_n.index(max(operatorstsall_n))-1]+'('+currentstring_11+')/'+currentstring_10
    else:currentstring = 'rank('+operatorsts[operatorstsall_n.index(max(operatorstsall_n))-1]+'('+currentstring_11+',50)/'+currentstring_10

    return currentstring



driver.get("https://websim.worldquantchallenge.com/simulate")
driver.implicitly_wait(30)
invite=driver.find_element_by_xpath("/html/body/main/article/div/div/div[3]/div/div[1]/div/div/form/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre")
invite.click()
field=driver.find_element_by_css_selector("div#code-editor-container > div > div > textarea")
field.send_keys(currentstring+' ')
field.send_keys(Keys.SHIFT,Keys.ENTER)
field.send_keys(Keys.ESCAPE)
driver.implicitly_wait(5)
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
driver.implicitly_wait(180)
result = driver.find_element_by_id("resultTabPanel")
driver.implicitly_wait(10)
sharpe=driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
sharpe.click()
sharpe=driver.find_element_by_xpath('/html/body/main/article/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody[1]/tr[7]/td[4]/span')
operatorstsall_n[0]=float(sharpe.text)
print(operatorstsall_n[0])






currentstring=ts_1(currentstring)
currentstring=ts_1(currentstring)
print(currentstring)

currentstring=ts_2(currentstring)
currentstring=ts_2(currentstring)
print(currentstring)

currentstring = ts_m(currentstring)
currentstring = ts_m(currentstring)
print(currentstring_final)








