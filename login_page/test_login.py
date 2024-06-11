import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from assertpy import assert_that

o = Options()
o.add_argument("--start-maximized")
o.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=o)
driver.implicitly_wait(15)
driver.get("https://qubisa.com")

driver.find_element(By.ID, "header-button-sign-in").is_displayed()
driver.find_element(By.ID, "header-button-sign-up").is_displayed()
driver.find_element(By.ID, "header-product-menu-desktop").is_displayed()
driver.find_element(By.ID, "header-button-sign-in").click()

driver.find_element(By.XPATH, "//input[@type='email']").is_displayed()
driver.find_element(By.XPATH, "//input[@type='password']").is_displayed()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("joshua@qubisa.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("qubisa123")
driver.find_element(By.ID, "sign-in").click()
url_after_login = driver.current_url
assert_that(url_after_login).is_equal_to("https://qubisa.com")


time.sleep(1)
driver.quit()