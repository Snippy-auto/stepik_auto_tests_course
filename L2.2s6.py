import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 200);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    btn1 = browser.find_element(By.ID, "robotCheckbox")
    btn1.click()

    btn2 = browser.find_element(By.ID, "robotsRule")
    btn2.click()

    btn3 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    btn3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()