import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("sobaka@sobaka.com")

    x_element = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Abracadabra__1_.txt')  # добавляем к этому пути имя файла
    x_element.send_keys(file_path)

    btn3 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    btn3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()