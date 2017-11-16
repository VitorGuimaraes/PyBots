#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from pprint import pprint
import telepot
import time
from datetime import datetime as dt

bot = telepot.Bot("337629525:AAHydEQ24w06_J8VTW7stcwb2FXmHw_ykyU")

driver = webdriver.PhantomJS()

def connected():
	driver.get("https://br.investing.com/crypto/currencies")
	try:
		driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[1]/td[4]")
		print "Conexão estabelecida"

	except:
		print "Tentando conexão..."
		time.sleep(1)
		connected()

def getBitcoin():
	return "BTC/USD - $" + str(driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[1]/td[4]").text.strip())

def getEthereum():
	return "ETH/USD - $" + str(driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[2]/td[4]").text.strip())

def getRipple():						
	return "XRP/USD - $" + str(driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[4]/td[4]").text.strip())

def getBitcoinCash():						
	return "BCH/USD - $" + str(driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[3]/td[4]").text.strip())

def getLitecoin():
	return "LTC/USD - $" + str(driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[5]/td[4]").text.strip())

def getOmiseGo():
	return "OMG/USD - $" + str(driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[17]/td[4]").text.strip())

def getIota():
	return "IOTA/USD - $" + str(driver.find_element_by_xpath(".//*[@id='top_crypto_tbl']/tbody/tr[7]/td[4]").text.strip())

def main(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	command = msg['text'].lower()
	print command

	if command == "/getprice" or command == "/getprice@theferacoinbot":
		start = dt.now()
		connected()
		bot.sendMessage(chat_id, getBitcoin() + '\n' +
								 getEthereum()+ '\n' +
								 getRipple()  + '\n' +
								 getBitcoinCash()  + '\n' +
								 getLitecoin()+ '\n' +
								 getOmiseGo() + '\n' +
								 getIota())
		print dt.now() - start

bot.message_loop(main)

while True:
	time.sleep(10)