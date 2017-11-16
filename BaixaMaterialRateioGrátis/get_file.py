#encoding: utf-8
#Este bot automatiza o download de materiais do site Rateio Grátis
#Basta iniciar o bot e acessar a área do aluno, e depois abrir
#a página do material que deseja baixar

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

file = open("file_name.txt", "w") 

def waitTime(delay):
	for i in reversed(range(delay)):
		minutos = i/60
		segundos = i - (minutos * 60)

		print("Aguardando: " + str(segundos) + " segundos")
		time.sleep(1)


def load(driver):
	try:
		driver.find_element_by_xpath(".//*[@id='menu-perfil']")
		print("\nPágina de cursos carregada!")

	except:
		print("\nAguardando página de cursos...")
		waitTime(10)
		load(driver)

def selectCourse(driver):
	try:
		driver.find_element_by_xpath(".//*[@id='div-aviso-escolha-conteudo']/span")
		print("\nCurso selecionado!")

	except:
		print("Escolha um curso...")
		time.sleep(5)
		selectCourse(driver)

def prepareToDownload(driver):
	try:
		driver.find_element_by_xpath(".//*[@id='ul-cronograma-curso']/li[1]/ul/li/div")
		print("\nIniciando downloads...\n")

	except:
		print("Preparando para iniciar download...")
		time.sleep(3)
		prepareToDownload(driver)

def downloadAula(driver, i):
	try:
		driver.find_element_by_xpath(".//*[@id='ul-cronograma-curso']/li[" + str(i)+ "]/ul/li/span[1]").click()
		time.sleep(3)
		btn = driver.find_element_by_xpath(".//*[@id='BotaoDownloadPDF']")
		time.sleep(2)
		aula = driver.find_element_by_xpath(".//*[@id='nome-conteudo']").text.strip()
		file.write(aula + os.linesep)
		print "baixando " + aula
		btn.click()
		return True

	except:
		print("Download Concluído!")
		time.sleep(2)
		return False

def backMainPage(driver):
	try:
		driver.find_element_by_xpath(".//*[@id='botao-voltar-para-home']").click()

	except:
		time.sleep(3)
		backMainPage(driver)

driver = webdriver.Firefox()
driver.get("https://rateiogratis.com.br")

while(True):
	load(driver)
	selectCourse(driver)
	prepareToDownload(driver)

	for i in range(1, 40):
		if downloadAula(driver, i) == False:
			break
		time.sleep(1)

	backMainPage(driver)
	file.close() 
	time.sleep(3)