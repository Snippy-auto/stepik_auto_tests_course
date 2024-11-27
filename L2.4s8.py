from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()


    x = browser.find_element(By.ID, "input_value").text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(int(x))

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()