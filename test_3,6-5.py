import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_login_in(browser, number):
    try:
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(link)

        browser.find_element(By.LINK_TEXT, "Войти").click()

        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("{login}")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("{password}")
        browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()

        time.sleep(7)

        answer_field = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
        answer = str(math.log(int(time.time())))
        answer_field.send_keys(answer)
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(2)

        x_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        x = x_element.text

        assert x == "Correct!", f"Текст сообщения {x}"

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
