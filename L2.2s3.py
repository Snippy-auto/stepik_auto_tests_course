import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    operator_element = browser.find_element(By.CSS_SELECTOR, "body > div > form > h2 > span:nth-child(3)")
    x = x_element.text
    y = y_element.text
    o = operator_element.text

    def parse_math_operation(x: int, o: str, y: int):
        if o == '+': return x + y
        if o == '-': return x - y
        if o == '*': return x * y
        if o == '/': return x / y

    s = parse_math_operation(int(x), o, int(y))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(s))

    btn3 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    btn3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()