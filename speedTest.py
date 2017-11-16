#encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random 
import os

def login(mainDriver):
	try:
		driver.find_element_by_class_name("js-username-field").send_keys("SEU_EMAIL") 
		time.sleep(1)
		driver.find_element_by_class_name("js-password-field").send_keys("SUA_SENHA")
		driver.find_element_by_xpath(".//*[@id='page-container']/div/div[1]/form/div[2]/button").click()
		print time.strftime('%H:%M:%S') + " Login realizado com sucesso"

	except:
		time.sleep(3)
		print time.strftime('%H:%M:%S') + " Aguardando login e senha..."
		login(mainDriver)

def tweet(mainDriver, fileName):
	try:
		mainDriver.find_element_by_xpath(".//*[@id='tweet-box-home-timeline']").send_keys("Oi velox muito lenta")
		time.sleep(5)
		mainDriver.find_element_by_css_selector('input.file-input').send_keys("C:\\Users\\Vitor\\Desktop\\speedTest\\" + fileName + ".png")
		time.sleep(3)
		driver.find_element_by_css_selector('button.tweet-action').click()

	except:
		tweet(mainDriver)

def waitLoad(mainDriver):
	try:
		mainDriver.find_element_by_id("speed-value")

	except:
		print time.strftime('%H:%M:%S') + " Aguardando carregamento da pagina..."
		time.sleep(2)
		waitLoad(mainDriver)

def doTest(mainDriver):
	speedTest = []
	condition = False

	while condition == False:
		for i in range(5):
			speedTest.insert(i, float(driver.find_element_by_id("speed-value").text.strip()))
			print "SpeedTest " + str(i) + " = " + str(driver.find_element_by_id("speed-value").text.strip())
			time.sleep(1)

		if speedTest[0] == speedTest[1] and speedTest[0] == speedTest[2] and speedTest[0] == speedTest[3] and speedTest[0] == speedTest[4]:
			condition = True
			print "Finished succesfull"
			return speedTest[0]

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")
login(driver)

driver.execute_script("window.open('https://fast.com/pt/');")
driver.switch_to_window(driver.window_handles[1])
#Espera o fast.com carregar
waitLoad(driver)

if doTest(driver) < 8.0:
	fileName = time.strftime('%d-%b-%y - %Hh%Mm%Ss')
	driver.save_screenshot("C:\\Users\\Vitor\\Desktop\\speedTest\\" + fileName + ".png")
	
	#Seleciona a aba do Twitter
	driver.switch_to_window(driver.window_handles[0])
	tweet(driver, fileName)