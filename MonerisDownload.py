from selenium import webdriver;
from selenium.webdriver.support.ui import Select;
import time;

# version: beta 0.9.1
# Last Update: Feb 23, 2022
# note: testing software, download Moneris Daily Transcation csv, no GUI

# change your Moneris Credential and Chain number here
MonerisUsername = 'username'
MonerisPassword = 'password'
ChainNumber = '000000000'

# change your DATE parameters here
curYear = '2021'
curMNTH = '12'
dates_curMNTH = ['20', '21','22']

# download Chrome WebDriver if upgraded

driver = webdriver.Chrome('./chromedriver96.exe')
# Login Moneris
driver.get('https://www1.moneris.com/cgi-bin/rbaccess/rbunxcgi?F6=1&F7=L8&F21=PB&F22=L8&REQUEST=ClientSignin&LANGUAGE=ENGLISH')
driver.find_element_by_name('USERID').send_keys(MonerisUsername)
driver.find_element_by_name('PASSWORD').send_keys(MonerisPassword)
driver.find_element_by_name('SignIn').click()
time.sleep(2)

# Navigate to Chain
driver.find_element_by_id('homebtnmd2').click()

# INPUT Super Chain Number here
driver.find_element_by_link_text(ChainNumber).click()
driver.find_element_by_class_name('button').click()
driver.find_element_by_name('FOCEXEC_LIST').click()

# loop starts
for date in dates_curMNTH:
  #Select Dates
  driver.find_element_by_name('FROMYEAR').send_keys(curYear)
  MNTH = Select(driver.find_element_by_name('FROMMTH'))
  MNTH.select_by_value(curMNTH)
  DATE = Select(driver.find_element_by_name('FROMDAY'))
  DATE.select_by_value(date)
  
  #Download CSV files
  driver.find_element_by_name('Download').click()
  driver.find_element_by_name('Download').click()
  driver.find_element_by_xpath("//input[@onclick='history.back(1)']").click()
  
# close browser
time.sleep(15)
driver.close()
