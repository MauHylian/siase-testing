from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configparser
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

configParser = configparser.RawConfigParser()
configFilePath = r'C:\Users\mauhy\Desktop\Escritorio\Programación\Python\siase-logger\config\config.txt'
configParser.read(configFilePath)
username = configParser.get("user-config", "username")
password = configParser.get("user-config", "password")

driver = webdriver.Chrome(r"C:\Users\mauhy\Desktop\Escritorio\Programación\Python\siase-logger\chromedriver.exe")

print(username)
print(password)


def login():
    # Abre Chrome e ingresa a la URL
    driver.get("https://deimos.dgi.uanl.mx/cgi-bin/wspd_cgi.sh/login.htm")

    # Encuentra los fields de input para cuenta y contraseña.
    # clear() se aplica en caso de que los campos tengan texto.
    driver.find_element_by_id("cuenta").clear()
    driver.find_element_by_id("pass").clear()

    # Se ingresan los valores de usuario y contraseña según
    # el archivo de config.
    driver.find_element_by_id("cuenta").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    time.sleep(2)
    print("click")

    # Se encuentra el botón de Entrar y da click.
    driver.find_element_by_xpath("/html/body/div/form/fieldset/div[4]/button").click()

    # Se gemera una lista de los elementos <a> en la página actual.
    # Página actual: Selección de servicio (SIASE / CORREO / NEXUS / CÓDICE)
    a_tags = driver.find_elements_by_tag_name("a")
    time.sleep(2)
    # print("click")
    # print(len(a_tags))
    a_tags[5].click() # Click en la carrera actual.

    # UNTESTED
    driver.find_element_by_id("li_Inscripción PROVERICYT").click() # Click en opcion PROVERICYT de menú lateral
    driver.find_element_by_name("").send_keys(Keys.RETURN) # Presionar tecla ENTER para proceder con el Pop-Up
    time.sleep(1)
    URL = driver.current_url
    print(URL)
    driver.close() # Teniendo la URL de PROVERICYT podemos close la página.

    # Scraping del promedio

    # Alternativa para conseguir el promedio mediante Selenium
    promedioSelenium = driver.find_element_by_id("htmlPromedio").text
    print(promedioSelenium)
    
    '''
    # Alternativa para conseguir el promedio mediante Beautiful Soup

    searchClient = uReq(URL)
    search_html = searchClient.read()
    searchClient.close()
    search_soup = soup(search_html, "html.parser")

    promedioSoup = search_soup.find("input", { "id" : "htmlPromedio" })
    print(promedioSoup)
    '''

login()
