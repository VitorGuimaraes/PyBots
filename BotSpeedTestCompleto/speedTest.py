# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

font = ImageFont.truetype("nyala.ttf", 20)
imgPath = "C:\\Users\\Vitor\\Desktop\\BotSpeedTest\\speedTest\\"
fakeTweets = []
trueTweets = []
contTweets = 0

#O arquivo de texto deve ser salvo como UTF-8
with open("fakeTweets.txt", "r") as file:
	for line in file:
		fakeTweets.append(line)

with open("trueTweets.txt", "r") as file:
	for line in file:
		trueTweets.append(line)

def showTime(delay, tweetsQuantity):
	for i in reversed(range(delay)):
		minutos = i/60
		segundos = i - (minutos * 60) 

		print("Proximo speedTest em " + str(minutos) + " minutos e " + str(segundos) + " segundos")
		print(str(tweetsQuantity) + " tweets foram enviados\n\n")
		time.sleep(1)

def login(mainDriver):
	try:
		driver.find_element_by_class_name("js-username-field").send_keys("driveextraa@hotmail.com")
		time.sleep(2)
		driver.find_element_by_class_name("js-password-field").send_keys("2345meia78")
		driver.find_element_by_xpath(".//*[@id='page-container']/div/div[1]/form/div[2]/button").click()
		print time.strftime('%H:%M:%S') + " Login realizado com sucesso"

	except:
		time.sleep(3)
		print time.strftime('%H:%M:%S') + " Aguardando login e senha..."
		login(mainDriver)

def tweet(mainDriver, fileName, _index, _id):
	#Gera um id aleatorio
	try:
		#Upload do printscreen
		mainDriver.find_element_by_css_selector('input.file-input').send_keys(imgPath + fileName + ".png")
		time.sleep(2)
		
		#Mensagem do tweet
		mainDriver.find_element_by_id('tweet-box-home-timeline').send_keys(unicode(trueTweets[_index], "utf-8") + "\n" + str(_id))  
		mainDriver.find_element_by_css_selector('button.tweet-action').click()

	except:
		print time.strftime('%H:%M:%S') + " Tentando tweetar novamente..."
		time.sleep(3)
		tweet(mainDriver, fileName, _index, _id)

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

	time.sleep(5)
	mainDriver.switch_to_window(driver.window_handles[1])
	mainDriver.get("https://fast.com/pt/")
	#Espera o fast.com carregar
	waitLoad(mainDriver)

	while condition == False:
		for i in range(3):
			speedTest.insert(i, float(driver.find_element_by_id("speed-value").text.strip()))
			print "SpeedTest " + str(i) + " = " + str(driver.find_element_by_id("speed-value").text.strip())
			time.sleep(2)

		if speedTest[0] == speedTest[1] and speedTest[0] == speedTest[2]:
			condition = True
			print "Finished speedTest succesfull!!! Speed = " + str(speedTest[0]) + "Mbps"
			return speedTest[0]

driver = webdriver.PhantomJS()
driver.get("https://twitter.com/login")
login(driver)

driver.execute_script("window.open('https://fast.com/pt/');")
while True:
	#Gera um tempo aleatorio
	delay = random.randrange(1800, 3600) 
	#Escolhe um tweet verdadeiro aleatoriamente
	nTrueTweet = random.randrange(0, len(trueTweets) - 1)
	#Escolhe um tweet falso aleatoriamente
	nFakeTweet = random.randrange(0, len(fakeTweets) - 1)
	#Cria um numero aleatorio
	_id = random.randrange(1, 5000)

	#Se a velocidade estiver abaixo de 8Mbps
	if doTest(driver) < 8.0:
		fileName = time.strftime('%d-%b-%y - %Hh%Mm%Ss')

		#Tira print da tela, edita e salva
		driver.save_screenshot(imgPath + fileName + ".png")
		img = Image.open(imgPath + fileName + ".png")
		draw = ImageDraw.Draw(img)
		draw.text((20, 20), fileName, (0, 0, 0), font = font)
		img.save(imgPath + fileName + ".png")

		#Seleciona a aba do Twitter
		driver.switch_to_window(driver.window_handles[0])
		driver.get("https://twitter.com/")
		tweet(driver, fileName, nTrueTweet, _id)
		
		contTweets += 1
		showTime(delay, contTweets)

	else:
		driver.switch_to_window(driver.window_handles[0])
		driver.get("https://twitter.com/intent/tweet?")
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='status']").send_keys(unicode(fakeTweets[nFakeTweet], "utf-8") + str(_id))
		#Clica para postar o tweet
		driver.find_element_by_xpath(".//*[@id='update-form']/div[3]/fieldset/input[2]").click()
		showTime(delay, contTweets)