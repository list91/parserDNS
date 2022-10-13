from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time


def script_pars(catalog_link, ages):
	err=0
	fael=open('test.txt', 'w', encoding="utf-8")
	chromedriver = 'chromedriver'
	options = webdriver.ChromeOptions()
	#options.add_argument('headless')  # для открытия headless-браузера
	browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
	start=catalog_link
	f=0
	catalogs=[]
	for age in range(1, int(ages)+1):#подготавливаем ссылки каждого каталога
		age='?p='+str(age)
		browser.get(start+age)
		requiredHtml = browser.page_source
		soup = BeautifulSoup(requiredHtml, 'lxml')
		cards=soup.find_all('a', class_='catalog-product__name')
		prices=soup.find_all('div', class_='product-buy__price')
		links=[]
		for card in cards:
			link="https://www.dns-shop.ru"+card.get('href')
			links.append(link)
		item=[]
		items=[]
		for p, l in zip(prices,links):
			if p==None:
				p='...'
				err=err+1
			else:
				p=p.text
			item=[]
			item.append(p)
			item.append(l)
			items.append(item)
			f=f+1
		catalogs.append(items)
#ПОЛУЧАЕМ ССЫЛКИ НА ВСЕ ТОВАРЫ СО ВСЕХ КАТАЛОГОВ
	n=0
	for catalog in catalogs:
		for items in catalog:
			if n>=f:
				break
			price=items[0]
			link=items[1]
			browser.get(link)
			requiredHtml = browser.page_source
			soup = BeautifulSoup(requiredHtml, 'lxml')
			lnx=soup.find_all('img')
			for i in lnx:
				img=i.get('src')
				break				
			if img==None:
				img="None"
				err=err+1
			title=soup.find('h1', class_='product-card-top__title')
			if title==None:
				err=err+1
				title="None"
			else:
				title=title.text
			n=n+1
			fael.write(str(n)+".\nНазвание товара:\n"+title+"\n\n")
			print("\n"+title+"\n")
			fael.write("Ссылка на превью товара:\n"+img+"\n\n")
			fael.write("Цена товара:\n"+str(price)+"\n\n")
			fael.write("Ссылка на товар:\n"+link+"\n---------------------------------\n")
			print("------------------------------------------------------------------------------------------------------")
			print(str(n)+'/'+str(f))
			
	fael.close()
	print('Колличество ошибок - '+str(err))


'''
ТЕСТОВАЯ ВЕРСИЯ
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time


def script_pars(catalog_link, ages):
	err=0
	#webdriver.set_window_size(12, 800)
	fael=open('test.txt', 'w', encoding="utf-8")
	chromedriver = 'chromedriver'
	options = webdriver.ChromeOptions()
	options.add_argument('headless')  # для открытия headless-браузера
	browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
	start=catalog_link
	f=0
	catalogs=[]
	for age in range(1, int(ages)+1):#подготавливаем ссылки каждого каталога
		age='?p='+str(age)
		print("---------\nБЕРЕМ ИНФУ С КАТАЛОГА "+age+"\n----------")
		browser.get(start+age)
		requiredHtml = browser.page_source
		soup = BeautifulSoup(requiredHtml, 'lxml')
		cards=soup.find_all('a', class_='catalog-product__name')
		prices=soup.find_all('div', class_='product-buy__price')
		links=[]
		for card in cards:
			link="https://www.dns-shop.ru"+card.get('href')
			links.append(link)
		item=[]
		items=[]
		for p, l in zip(prices,links):
			if p==None:
				p='...'
				err=err+1
			else:
				p=p.text
			item=[]
			item.append(p)
			item.append(l)
			items.append(item)
			f=f+1
		catalogs.append(items)
		
		print(catalogs)
		print(len(catalogs))
		print(len(items))
	for i in catalogs:
		print(i)
		print("============================================================#2B2436")
	
	for i in catalogs:
		elem=0
		for j in i:
			elem=elem+1
			print("\nЭЛЕМЕНТ ИЗ КАТАЛОГА №"+str(elem))
			print(j)
		print("===========КОНЕЦ КАТАЛОГА============\n")
			
#ПОЛУЧАЕМ ССЫЛКИ НА ВСЕ ТОВАРЫ СО ВСЕХ КАТАЛОГОВ
	n=0
	for catalog in catalogs:
		for items in catalog:
			if n>=f:
				print("ДЕЛАЕМ БРЕЙК")
				break
			price=items[0]
			link=items[1]
			browser.get(link)
			requiredHtml = browser.page_source
			soup = BeautifulSoup(requiredHtml, 'lxml')
			lnx=soup.find_all('img')
			for i in lnx:
				img=i.get('src')
				break				
			if img==None:
				img="None"
				err=err+1
			title=soup.find('h1', class_='product-card-top__title')
			if title==None:
				err=err+1
				title="None"
			else:
				title=title.text
			n=n+1
			fael.write(str(n)+".\nНазвание товара:\n"+title+"\n\n")
			print("\n"+title+"\n")
			fael.write("Ссылка на превью товара:\n"+img+"\n\n")
			fael.write("Цена товара:\n"+str(price)+"\n\n")
			fael.write("Ссылка на товар:\n"+link+"\n---------------------------------\n")
			print("------------------------------------------------------------------------------------------------------")
			print(str(n)+'/'+str(f))
			
	fael.close()
	print('Колличество ошибок - '+str(err))
'''


#script_pars('https://www.dns-shop.ru/catalog/c0deef7739157fd7/plity-elektricheskie/',1)
#os.system('test.txt')


