import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from banco import insertPaises, insertProducao
def validar(texto):
	if texto[-1] == "%":
		texto = texto[:-1]
	return texto

def extrair_inteiro(texto):
	try:
		# Às vezes, esse valor pode iniciar pelo ano...
		i = texto.find(' ')
		if i >= 0:
			texto = texto[(i + 1):]

		sem_virgula = texto.replace(',', '')

		return float(sem_virgula)
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
ano = int(coluna_ano.text)

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

for linha in linhas:
		colunas = linha.find_elements_by_tag_name('td')
		colunas[1] = extrair_inteiro(validar(colunas[1].text))
		
		dado = [colunas[0].text, colunas[1], ano]
		insertProducao(paises,dado)
	

	# arrastar e ir para o próximo ano


driver.close()

