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
        nome = "Jãozinho"
        sobre_nome = "da Silva"
        instituiçao = "Objetivo"
        email = "jaozinhodasilva@abcbolinhas.com"
        user = "jaozinho"
        senha = "123"

    case 'login2':
        nome = "Jãozinho"
        sobre_nome = "da Silva"
        instituiçao = "Objetivo"
        email = "jaozinhodasilva@abcbolinhas.com"
        user = "jaozinho"
        senha = "123"

    
    case 'login3':
        nome = "Jãozinho"
        sobre_nome = "da Silva"
        instituiçao = "Objetivo"
        email = "jaozinhodasilva@abcbolinhas.com"
        user = "jaozinho"
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

        driver.get('https://www.gridlastic.com/register.php')
        t.sleep(10)
        driver.maximize_window()

        # Informaçõe usadas durante o código, como login, senha, usuário de procura

        try:
            campo_nome = driver.find_element(By. XPATH, '/html/body/div[2]/form/div[1]/div/div/input')
            campo_nome.send_keys(nome)

            print("Nome preenchido")
            t.sleep(3)

            campo_sobrenome = driver.find_element(By. XPATH, '/html/body/div[2]/form/div[2]/div/div/input')
            campo_sobrenome.send_keys(sobre_nome)

            print("Sobrenome preenchido")
            t.sleep(3)

            campo_instituicao = driver.find_element(By. XPATH, '/html/body/div[2]/form/div[3]/div/div/input')
            campo_instituicao.send_keys(instituiçao)

            print("Instituição preenchida")
            t.sleep(3)

            campo_email = driver.find_element(By. XPATH, '/html/body/div[2]/form/div[4]/div/div/input')
            campo_email.send_keys(email)

            print("E-mail preenchido")
            t.sleep(3)

            campo_username = driver.find_element(By. XPATH, '/html/body/div[2]/form/div[5]/div/div/input')
            campo_username.send_keys(user)

            print("User preenchido")
            t.sleep(3)

            campo_senha = driver.find_element(By. XPATH, '//*[@id="register_password"]')
            campo_senha.send_keys(senha)

            print("Senha preenchida")
            t.sleep(3)

            print("Cadastro Finalizado com sucesso")

            t.sleep(300)

            bota_criarconta =  driver.find_element(By. XPATH, '//*[@id="register-submit-btn"]')
            bota_criarconta.click()
                
        except Exception as e:
                print(e)
                #Esse print ele informa qual o nome do erro que esta condito dentro TryExpept

inicializaçao()