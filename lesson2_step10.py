from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"),"100")
    )
    button = browser.find_element(By.XPATH, "//button[@id='book']")
    button.click()

    message = browser.find_element(By.XPATH, "//button[@id='book']")


    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, "//input[@class='form-control' and @required]")
    input.send_keys(y)

    button = browser.find_element(By.XPATH, "//*[@id='solve']")
    button.click()

finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла