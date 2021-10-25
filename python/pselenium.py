import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from banco import insertPaises, insertProducao

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

cabecalho_tabela = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'table.data-table > thead'))
)

linhas = cabecalho_tabela.find_elements_by_tag_name('tr')

colunas = linhas[1].find_elements_by_tag_name('th')

coluna_ano = colunas[0]

corpo_tabela = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'table.data-table > tbody'))
)

linhas = corpo_tabela.find_elements_by_tag_name('tr')

# listar países e inserir
nomes = []
for linha in linhas:
	colunas = linha.find_elements_by_tag_name('td')
	nomes.append(colunas[0].text)

paises = insertPaises(nomes)

while coluna_ano < 2020:
	for linha in linhas:
		colunas = linha.find_elements_by_tag_name('td')

		
		dado = [colunas[0].text, colunas[1].text, coluna_ano]
		insertProducao(paises,dado)
	

	# arrastar e ir para o próximo ano


driver.close()

