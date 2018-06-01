from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.amazon.com")
search = driver.find_element_by_name("field-keywords")
search.send_keys("bikes")
driver.find_element_by_css_selector('input.nav-input').click()
driver.find_element_by_xpath("//div[@id='leftNavContainer']/ul[6]/div/li[5]/span/span/div/label/span").click()
