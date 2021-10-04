import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from banco.py import insertAno
from banco.py import insertPais
from banco.py import insertDado

def extrair_inteiro(texto):
	try:
		i = texto.rindex(' ')
		sem_unidade = texto[:i]

		# Às vezes, esse valor pode iniciar pelo ano...
		i = sem_unidade.find(' ')
		if i >= 0:
			sem_unidade = sem_unidade[(i + 1):]

		sem_virgula = sem_unidade.replace(',', '')

		return int(sem_virgula)
	except:
		return 0

driver = webdriver.Chrome()
driver.get('https://ourworldindata.org/renewable-energy')

botao_cookie = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-track-note="cookie-notice"]'))
)

# Às vezes o botão não era clicável de verdade logo de primeira 😅 ...
time.sleep(2)

botao_cookie.click()

botoes_tabela = WebDriverWait(driver, 20).until(
	EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-track-note="chart-click-table"]'))
)

botoes_tabela[0].click()

corpo_tabela = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'table.data-table > tbody'))
)

linhas = corpo_tabela.find_elements_by_tag_name('tr')



for linha in linhas:
	colunas = linha.find_elements_by_tag_name('td')

	nome = colunas[0].text
	valor1900 = colunas[1].text
	valor2019 = colunas[2].text
	dado = [nome, valor1900, linha['ano']]
	insertAno(linhas['ano'])
	insertPais(nome)
	insertDado(dado)



driver.close()
#x path tabela -> /html/body/main/article/div[3]/div[2]/div/div/section[2]/div[2]/div[1]/figure/div/div[2]/div[2]/nav/ul/li[3]/a
