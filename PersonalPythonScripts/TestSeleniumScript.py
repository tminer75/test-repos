from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://streamlegends.com/t/proletariat_inc/popout')
browser.add_cookie({'name': 'auth-token-v1', 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja2luZ19pZCI6IjlKQ2FJSWNPTDMiLCJ0d2l0Y2hfaWQiOiIxMDI0NzI5NDYifQ.srNWnHvi56Y2Is9jeVWdmNr5QHWfP4pM4aDden0762E'})
browser.refresh()
time.sleep(3)

# assert 'proletariat_inc | StreamLegends' in browser.title

'''
elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
'''

navTabElement = browser.find_element_by_xpath("//*[@id=\"srpg-nav-tab-CHARACTER\"]")
navTabElement.click()
time.sleep(3)

navTabElement = browser.find_element_by_xpath("//*[@id=\"srpg-nav-tab-GEAR\"]")
navTabElement.click()
bagColor = browser.find_element_by_xpath("/html/body/div/div/section/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[6]/div/div").value_of_css_property("color")
print(bagColor)
bagClassName = browser.find_element_by_xpath("/html/body/div/div/section/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[6]/div/div").value_of_css_property("class")
print(bagClassName)
time.sleep(3)

navTabElement = browser.find_element_by_xpath("//*[@id=\"srpg-nav-tab-FIGHT\"]")
navTabElement.click()
time.sleep(3)

navTabElement = browser.find_element_by_xpath("//*[@id=\"srpg-nav-tab-GUILD\"]")
navTabElement.click()
time.sleep(3)

navTabElement = browser.find_element_by_xpath("//*[@id=\"srpg-nav-tab-RANK\"]")
navTabElement.click()
time.sleep(3)

#browser.quit()

'''
I hold all of the copy/paste xpaths

/html/body/div/div/section/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[6]
/html/body/div/div/section/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[6]/div


'''