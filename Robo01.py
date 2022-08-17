from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os as os
import requests as requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
import pandas as pd
import pyautogui as p
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


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


# Essa parte é responsavel por abrir o driver e ir até a pasta desejada
def inicializaçao():


        # Iniciando o Chorme (driver de preferencia, mas RPA chrome é o recomendado)
        # Setando o link que o driver deve abrir 

        options = Options()
        options.add_argument("start-maximized")
        prefs = {"download.default_directory": "C:\\Users\\Wind Digital\\Downloads"}
        options.add_experimental_option("prefs", prefs)
        options.add_argument(
            'user-data-dir=C:\\Users\\Wind Digital\\AppData\\Local\\Google\\Chrome\\User Data')
        options.add_argument('profile-directory=Profile')
        driver = webdriver.Chrome(chrome_options=options, service=Service(ChromeDriverManager().install()))

        driver.get('https://www.instagram.com/')
        t.sleep(10)
        driver.maximize_window()

        # Informaçõe usadas durante o código, como login, senha, usuário de procura
        user = 'regis'
        senha = ''

        usuario_pesquisar = 'eita_regis'

        try:

                #Seletor do campo desejado para informar o que queremos fazer
                #Seletor #Path - //*[@id="loginForm"]/div/div[1]/div/label/input
                campo_login = driver.find_element(By. XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
                campo_login.send_keys(user)
                
                #Seletor #CSS Selector - #loginForm > div > div:nth-child(1) > div > label > input
                campo_login2 = driver.find_element(By. CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
                
                #Seletor #ClassName 
                campo_login3 = driver.find_element(By. CLASS_NAME, '#login')

                #Seletor #Id
                campo_login4 = driver.find_element(By. ID, 'login')

                #Campo de preenchimento de senha
                campo_senha = driver.find_element(By. XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
                campo_senha.send_keys(senha)

                botao_entrar = driver.find_element(By. XPATH, '#loginForm > div > div:nth-child(3) > button')

                if botao_entrar != None:
                        botao_entrar.click()
                
                else:
                        print('O login está incorreto')

        except Exception as e:
                print(e)
                #Esse print ele informa qual o nome do erro que esta condito dentro TryExpept

inicializaçao()