from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Entro na Página de cadastro de produto')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")


@when(u'faço login') 
def step_impl(context):
    context.driver.find_element(By.ID , "mui-1").send_keys("alle_andrade123@hotmail.com")
    context.driver.find_element(By.ID , "outlined-adornment-password").send_keys("050290")

@when(u'Efetuo login') 
def step_impl(context):
    botao_enviar = WebDriverWait(context.driver, 6).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/form/button"))
    )
    context.driver.execute_script("arguments[0].click();", botao_enviar)

@when(u'clico em adicionar')
def step_impl(context):
    botao_enviar = WebDriverWait(context.driver, 6).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/header/section[2]/div/header/button"))
    )
    context.driver.execute_script("arguments[0].click();", botao_enviar)


@when(u'preencho os dados do produto')
def step_impl(context):
    context.driver.find_element(By.ID , "mui-2").send_keys("Camiseta Verde")
    context.driver.find_element(By.ID , "mui-3").send_keys("Pequena")
    botao_roupa = WebDriverWait(context.driver, 6).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[1]"))
    )
    context.driver.execute_script("arguments[0].click();", botao_roupa)
    context.driver.find_element(By.ID , "mui-4").send_keys("35,60")
    
@when(u'Faço o upload da imagem "{image_path}"')
def step_impl(context, image_path): 
    upload_element = context.driver.find_element(By.XPATH, "//input[@type='file']") 
    upload_element.send_keys(image_path)
    context.driver.find_element(By.ID , "mui-6").send_keys("15,00")


@when(u'salvo os dados')
def step_impl(context):
    botao_salvar = WebDriverWait(context.driver, 6).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/button"))
    )
    context.driver.execute_script("arguments[0].click();", botao_salvar)