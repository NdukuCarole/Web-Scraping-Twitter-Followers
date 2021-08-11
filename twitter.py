#import
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,NoSuchElementException
twitter_handle = input('Please input your Twitter handle here: ')
#
driver = webdriver.Firefox()
driver.implicitly_wait(100)
try:
    driver.get('http://twitter.com/'+twitter_handle)
except WebDriverException as e:
    print("An error occured ", e)
else:
    try:
        web_element = driver.find_element_by_xpath('//a[@href="/' + twitter_handle + '/followers"]')
    except NoSuchElementException as e:
        print("An error occured ", e)
    else:
        print (web_element.text)
        #method to close & destroy both the WebDriver and Web Browser instances gracefully after each run of Test Execution.
        driver.quit()