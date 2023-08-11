from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


driver=webdriver.Firefox()


driver.get("https://phptravels.com/demo/")

#driver.find_element(By.NAME, "email_input").clear()
driver.find_element(By.NAME, "first_name").send_keys("gokce" )
driver.find_element(By.NAME, "last_name").send_keys("coban" )
driver.find_element(By.NAME, "business_name").send_keys("student" )
driver.find_element(By.NAME, "email").send_keys("bilbobagginspiposu@gmail.com" )


numb1 = driver.find_element(by=By.XPATH, value="//span[@id = 'numb1']").get_attribute('textContent')
numb2 = driver.find_element(by=By.XPATH, value="//span[@id = 'numb2']").get_attribute('textContent')
numb11=int(numb1)
numb22=int(numb2)
result=numb22+numb11

driver.find_element(By.ID, "number").send_keys(result)
driver.find_element(By.ID, "demo").click()
driver.find_element(By.LINK_TEXT, "Signup").click()



driver.get("https://phptravels.org/register.php")
driver.find_element(By.ID, "inputFirstName").click()
driver.find_element(By.ID, "inputFirstName").send_keys("FSgD")
driver.find_element(By.NAME, "lastname").send_keys("bagginss" )
driver.find_element(By.NAME, "email").send_şkeys("bilbooooo@gmail.com" )
driver.find_element(By.ID, "inputPhone").click()

country_select = Select(driver.find_element(By.ID, "inputCountry"))
country_select.select_by_visible_text("Morocco")
driver.find_element(By.ID, "inputPhone").send_keys("555555555")

driver.find_element(By.ID, "inputCompanyName").click()
driver.find_element(By.ID, "inputCompanyName").send_keys("ddfdd")
driver.find_element(By.ID, "inputAddress1").click()
driver.find_element(By.ID, "inputAddress1").send_keys("ddfdd")
driver.find_element(By.ID, "inputAddress2").click()
driver.find_element(By.ID, "inputAddress2").send_keys("ddfdd")
driver.find_element(By.ID, "inputCity").click()
driver.find_element(By.ID, "inputCity").send_keys("ddfdd")
driver.find_element(By.ID, "stateinput").click()
driver.find_element(By.ID, "stateinput").send_keys("dddd")
driver.find_element(By.ID, "inputPostcode").click()
driver.find_element(By.ID, "inputPostcode").send_keys("ddd")



country_select_icon = driver.find_element(By.ID, "inputCountryIcon")


sleep(1)
driver.find_element(By.ID, "customfield2").click()
driver.find_element(By.ID, "customfield2").send_keys("5071154855")
driver.find_element(By.ID, "inputNewPassword1").click()
driver.find_element(By.ID, "inputNewPassword1").send_keys("12345")
driver.find_element(By.ID, "inputNewPassword2").click()
driver.find_element(By.ID, "inputNewPassword2").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, ".bootstrap-switch-label").click()
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, ".btn-large").click()


driver.get("https://phptravels.org/login")
driver.find_element(By.ID, "inputEmail").click()
driver.find_element(By.ID, "inputEmail").send_keys("bilbooooo@gmail.com")
driver.find_element(By.ID, "inputPassword").click()
driver.find_element(By.ID, "inputPassword").send_keys("12345")
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
driver.switch_to.default_content()

driver.find_element(By.ID, "login").click()







