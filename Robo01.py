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


# Case são exatamente isso, cases, informações em blocos para serem selecionadas antes do codigo

login = "login1"

match login: 
    case 'login1':
        login = "abcbolinbhas123"
        senha = "123"

    case 'login2':
        login = "abcbolinbhas123"
        senha = "123"
    
    case 'login3':
        login = "abcbolinbhas123"
        senha = "123"

    case 'login4':
        login = "abcbolinbhas123"
        senha = "123"

####### Inicio do código ######

link = 'https://www.instagram.com/'

options = ChromeOptions()
path_chromedriver = "C:\Chrome Driver\chromedriver.exe"
prefs = {"download.default_directory": "C:\\Macros\\download"}
options.add_experimental_option("prefs", prefs)
navegador = Chrome(chrome_options=options)

# Essa parte é responsavel por abrir o navegador e ir até a pasta desejada

def inicializaçao():


        # Iniciando o Chorme (navegador de preferencia, mas RPA chrome é o recomendado)
        # Setando o link que o navegador deve abrir 
        navegador.get = link
        navegador.maximize_window()

        # Informaçõe usadas durante o código, como login, senha, usuário de procura
        user = ''
        senha = ''

        usuario_pesquisar = 'eita_regis'

        try:

                #Seletor do campo desejado para informar o que queremos fazer
                #Seletor #Path - //*[@id="loginForm"]/div/div[1]/div/label/input
                campo_login = navegador.find_element(By. XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
                campo_login.send_keys(user)
                
                #Seletor #CSS Selector - #loginForm > div > div:nth-child(1) > div > label > input
                campo_login2 = navegador.find_element(By. CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
                
                #Seletor #ClassName 
                campo_login3 = navegador.find_element(By. CLASS_NAME, '#login')

                #Seletor #Id
                campo_login4 = navegador.find_element(By. ID, 'login')

                #Campo de preenchimento de senha
                campo_senha = navegador.find_element(By. XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
                campo_senha.send_keys(senha)

                botao_entrar = navegador.find_element(By. XPATH, '#loginForm > div > div:nth-child(3) > button')

                if botao_entrar != None:
                        botao_entrar.click()
                
                else:
                        print('O login está incorreto')

        except Exception as e:
                print(e)
                #Esse print ele informa qual o nome do erro que esta condito dentro TryExpept

