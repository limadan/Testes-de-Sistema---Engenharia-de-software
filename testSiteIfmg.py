import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSiteIfmg(unittest.TestCase):
    def setUp(self):
        # Configurando o navegador (no exemplo, será o Firefox)
        self.driver = webdriver.Firefox()

    def test_ifmg_meuIF(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        linkmeuIF = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/ul/li[1]/a"))
        )
        linkmeuIF.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("RM Portal - Login Versão 12.1.2302.212")
        )

        self.assertIn("RM Portal - Login Versão 12.1.2302.212", self.driver.title)

    def test_Cpa(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        linkmeucpa = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/ul/li[2]/a"))
        )
        linkmeucpa.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Vestibular IFMG")
        )

        self.assertIn("Vestibular IFMG", self.driver.title)

    def test_webmail(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        linkwebmail = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/ul/li[3]/a"))
        )
        linkwebmail.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Gmail")
        )

        self.assertIn("Gmail", self.driver.title)

    def test_contato(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        linkcontato= WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/ul/li[4]/a"))
        )
        linkcontato.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Contato — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais Campus Sabará")
        )

        self.assertIn("Contato — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais Campus Sabará", self.driver.title)

    def test_exalunos(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        linkexalunos = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/ul/li[5]/a"))
        )
        linkexalunos.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Formulário Contato Ex alunos — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais Campus Sabará")
        )

        self.assertIn("Formulário Contato Ex alunos — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais Campus Sabará", self.driver.title)

    def test_acessoaSistemas(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        linkAcessoASistemas = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/ul/li[6]/a"))
        )
        linkAcessoASistemas.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Acesso a Sistemas — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais IFMG")
        )

        self.assertIn("Acesso a Sistemas — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais IFMG", self.driver.title)

    def test_busca(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        inputBusca = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/form/fieldset/input[1]"))
        )
        inputBusca.send_keys("Teste")
        inputBusca.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Busca — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais Campus Sabará")
        )

        spanBusca = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div/form/div[1]/div[1]/h1/strong/span")

        self.assertIn("Teste", spanBusca.text)

    def tearDown(self):
        # Encerrando o navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
