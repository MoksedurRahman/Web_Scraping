from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "https://immobilier.jll.fr/location-entrepot/entrepot-a-louer-marly-la-ville-95670-667005"

def get_hidden_text():
    # Here is the path of Webdriver
    #driver = webdriver.Chrome("")
    driver = webdriver.Chrome("c:\\chromedriver.exe")
    driver.get(url)
    
    #Description
    print()
    print('==========Description============')
    button = driver.find_element(By.CLASS_NAME, "ToggleContentButton")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    # descriptions=driver.find_element(By.CLASS_NAME,'ToggleContent__inner').text
    # print(descriptions)
    
    descriptions=driver.find_element(By.CLASS_NAME,'ToggleContent__inner')
    elements = descriptions.find_elements(By.TAG_NAME, 'p')
    for e in elements:
        print(e.text)
    print()
    
    #Prestations & Services
    print('==========Prestations & Services============')
    Services = driver.find_element(By.CLASS_NAME, "PropertyDetailsPage__collapse-toggle")
    driver.execute_script("arguments[0].click();", Services)
    
    time.sleep(5)
    Services_text=driver.find_element(By.CLASS_NAME,'TickList')
    elements = Services_text.find_elements(By.TAG_NAME, 'li')
    for e in elements:
        print(e.text)
    print()
    
    #Name    
    print('==========Name============')
    time.sleep(5)
    BrokersDetails__name=driver.find_element(By.CLASS_NAME,'BrokersDetails__name').text
    print(BrokersDetails__name)
    print()
    
    #Contact
    print('==========Contact============')
    time.sleep(5)
    BrokersDetails__telephone=driver.find_element(By.CLASS_NAME,'BrokersDetails__button--telephone').text
    print(BrokersDetails__telephone)
get_hidden_text()