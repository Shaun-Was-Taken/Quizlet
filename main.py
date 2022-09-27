from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(
    executable_path="driver\chromedriver.exe")
driver.minimize_window()
driver.implicitly_wait(0.5)
# driver.maximize_window()
driver.get('url')
driver.find_element(
    By.CLASS_NAME, 'SiteNavLoginSection-loginButton').click()
element = driver.find_element(By.ID, 'username')
element.send_keys("Your Email Here")
element = driver.find_element(By.ID, 'password')
element.send_keys("Your Password Here")
driver.find_element(
    By.CLASS_NAME, 'UILoadingButton').click()
driver.find_element(By.CLASS_NAME, 'b6g4t1k').click()
g = open('answer.html', 'a', encoding='utf-8')
g.write(driver.page_source)
g.close()
