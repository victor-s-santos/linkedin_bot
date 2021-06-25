from selenium import webdriver
from decouple import config
from selenium.webdriver.firefox.options import Options
import time

"""Variaveis de ambiente"""
email = config('EMAIL')
senha = config('PASSWORD')
delay = 3

def linkedin_bot(perfil_link):
    """Inicializa o processo do selenium"""
    global email, senha, delay
    url = 'https://www.linkedin.com/login'
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option)
    driver.get(url)
    #realizando o login
    #usuario
    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys(email)
    #senha
    password = driver.find_element_by_name("session_password")
    password.clear()
    password.send_keys(senha)
    #realizando o click para logar
    driver.find_element_by_xpath("//button[@type='submit']").click()
    print("Login realizado com sucesso!")
    try:
        driver.find_element_by_id("remember-me-prompt__form-secondary").click()
        print("Definido para não lembrar senha.")
    except:
        print("Não necessário!")
    
    #adiciona pefil
    driver.get(perfil_link)
    driver.find_element_by_xpath('//div[@class="pvs-profile-actions "]//button[@class="pvs-profile-actions__action artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]').click()
    #envia
    time.sleep(3)
    driver.find_element_by_xpath('//button[@aria-label="Enviar agora"]').click()


#linkedin_bot()
def printa(arquivo):
    file = open(arquivo, 'r')
    list_of_lines = file.readlines()
    file.close()
    for line in list_of_lines:
        print(line)

printa('links_usuarios.txt')