import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(int(x))

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()