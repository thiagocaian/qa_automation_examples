from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_login_invalid():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    # Preenche login inválido (senha errada)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Espera a mensagem de erro aparecer
    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "Your password is invalid!" in flash.text

    driver.quit()
