import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGoogleDoodles(unittest.TestCase):
    def setUp(self):
        # Configurando o navegador (no exemplo, será o Firefox)
        self.driver = webdriver.Firefox()

    def test_google_doodles(self):
        self.driver.get("https://www.google.com")

        # Verifique o botão "Estou com sorte"
        btn_estou_com_sorte = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]"))
        )
        btn_estou_com_sorte.click()

        # Aguardar até que a página de Doodles esteja visível
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Doodles")
        )

        # Verificar se "Google Doodles" está no título da página
        self.assertIn("google doodles", self.driver.title.lower())
        
    def tearDown(self):
        # Encerrando o navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
