from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os as os
import requests as requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
import pandas as pd
import pyautogui as p
import pdfplumber as pdfplumber
import re
from collections import namedtuple
import json
import time as t

url = 'https://bnccompras.com/Process/ProcessSearchPublic?param1=1'


options = ChromeOptions()
path_chromedriver = "C:\Projeto\chromedriver.exe"
prefs = {"download.default_directory": "C:\\Macros\\download"}
options.add_experimental_option("prefs", prefs)


####### Inicio do código ######

# Essa parte é responsavel por abrir o navegador e ir até a pasta desejada

def inicialização (data) -> None:
    
    # Iniciando o Chorme (navegador de preferencia, mas RPA chrome é o recomendado)
    navegador = Chrome(
            options=options, executable_path=f"{path_chromedriver}")
    
    # Setando o link que o navegador deve abrir 
    navegador.get = 'https://www.instagram.com/'

    # Informaçõe usadas durante o código, como login, senha, usuário de procura
    user = ''
    senha = ''

    usuario_pesquisar = 'eita_regis'

    #Seletor do campo desejado para informar o que queremos fazer
    #Seletor #Path - //*[@id="loginForm"]/div/div[1]/div/label/input
    campo_login = navegador.find_element(By. XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    
    #Seletor #CSS Selector - #loginForm > div > div:nth-child(1) > div > label > input
    campo_login = navegador.find_element(By. CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
    
    #Seletor #ClassName 
    campo_login = navegador.find_element(By. CLASS_NAME, '#login')

    #Seletor #Id
    campo_login = navegador.find_element(By. ID, 'login')


    campo_login.send_keys(user)

    



