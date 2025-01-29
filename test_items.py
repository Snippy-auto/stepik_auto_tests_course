from selenium.webdriver.common.by import By

def test_guest_should_see_add_button(browser, language):
    browser.get(language)
    add_button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert add_button.is_displayed(), "Кнопка добавления не найдена"
