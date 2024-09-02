import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginHerokuapp(unittest.TestCase):
    def setUp(self):
        # Configurando o navegador (no exemplo, será o Firefox)
        self.driver = webdriver.Firefox()

    def test_login(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

        # Verifique o campo "username"
        username = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/div[1]/div/input"))
        )
        username.send_keys("tomsmith")

        password = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/div[2]/div/input"))
        )
        password.send_keys("SuperSecretPassword!")


        btn_login = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/button"))
        )
        btn_login.click()


        WebDriverWait(self.driver, 20)

        self.assertIn("https://the-internet.herokuapp.com/secure", self.driver.current_url)
    
    def test_error_login(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

        # Verifique o campo "username"
        username = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/div[1]/div/input"))
        )
        username.send_keys("tomsmith")

        password = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/div[2]/div/input"))
        )
        password.send_keys("adsfdaf!")


        btn_login = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/button"))
        )
        btn_login.click()


        WebDriverWait(self.driver, 20)

        self.assertIn("https://the-internet.herokuapp.com/login", self.driver.current_url)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
