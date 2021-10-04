import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://ourworldindata.org/renewable-energy')


botao_cookie = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.accept'))
)
# Às vezes o botão não era clicável de verdade logo de primeira 😅 ...
time.sleep(2)

botao_cookie.click()

botoes_tabela = WebDriverWait(driver, 20).until(
	EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-track-note="chart-click-table"]'))
)
# botoes_tabela[1].click()
botoes_tabela[0].click()

corpo_tabela = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'table.data-table > tbody'))
)

linhas = corpo_tabela.find_elements_by_tag_name('tr')

dados = []

for linha in linhas:
	colunas = linha.find_elements_by_tag_name('td')

	nome = colunas[0].text
	valor1900 = colunas[1].text
	valor2019 = colunas[2].text
	print(nome, valor1900, valor2019)

    
# linhas = corpo_tabela.find_elements_by_tag_name('tr')

# dados = []

# for linha in linhas:
# 	colunas = linha.find_elements_by_tag_name('td')

# 	nome = colunas[0].text
# 	valor1900 = colunas[1].text
# 	valor2019 = colunas[2].text

# 	dados.append({
# 		'nome': nome,
# 		'valor1900': extrair_inteiro(valor1900),
# 		'valor2019': extrair_inteiro(valor2019)
# 	})

# print(dados)

# driver.close()
