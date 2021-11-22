'https://stackoverflow.com/questions/68198511/scroll-element-horizontally-selenium-python'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "https://www.morningstar.com/stocks/xnas/tsla/financials"
driver.get(url)
driver.maximize_window()
# Click on Income Statement
xpath = '//*[@id="__layout"]/div/div[2]/div[3]/main/div[2]/div/div/div[1]/sal-components/section/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/a'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
# click on More Financials Detail Data
xpath = '//*[@id="__layout"]/div/div[2]/div[3]/main/div[2]/div/div/div[1]/sal-components/section/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/a'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

xpath='/html/body/main/article/div[3]/div[2]/div/div/section[2]/div[2]/div[1]/figure/div/div[2]/div[1]/div/div[3]/div[1]'
horizontal_bar_width = driver.find_element_by_xpath(xpath).rect['width']
slider = driver.find_element_by_xpath(xpath)
ActionChains(driver).click_and_hold(slider).move_by_offset(horizontal_bar_width/2, 0).release().perform()