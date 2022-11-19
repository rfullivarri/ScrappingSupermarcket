from ast import While
from lib2to3.pgen2 import driver
from turtle import title
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
import pandas as pd
import sqlite3


#def SCP_Disco ():
Options= webdriver.ChromeOptions()
Options.add_argument("--start-maximized")
   
Driver= webdriver.Chrome(r"/Users/ramirofernandezdeullivarri/opt/rulo/newvenv/Webdriver/chromedriver" , options=Options)

Driver.get("https://www.disco.com.ar/almacen")
#Driver.maximize_window()

WebDriverWait(Driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH,"//button[@class='align-right secondary slidedown-button']")))\
   .click()

time.sleep(2)

# WebDriverWait(Driver, 5)\
#    .until(EC.element_to_be_clickable((By.XPATH,"//div[@class='categoryList-container']//a[@class='categoryList__viewAll']")))\
#    .click()

# time.sleep(1)

productos, nombres, marcas, precios= [],[],[],[]
i= 1

for i in range(1,3):
 #LOOP PARA CARGAR PAGINAS DE PRODUCTOS  
 Driver.get("https://www.disco.com.ar/almacen?map=category-1&page={}".format(i))
 time.sleep(5)

 #SCROLLEAR PARA ABAJO
 y = 1000
 for timer in range(0,3):
      Driver.execute_script("window.scrollTo(0, "+str(y)+")")
      y += 1000  
      time.sleep(1)

 #CARGAR  LINKS DE LOS PRODUCTOS
 productos1 = Driver.find_elements(By.XPATH,"//div[@id='gallery-layout-container']//div[@class='vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--grid pa4']//a[@class='vtex-product-summary-2-x-clearLink h-100 flex flex-column']")
 print("Encontro ",len(productos1), "productos")
 productos1 = [producto.get_attribute('href') for producto in productos1]
 productos.extend(productos1)

 #INGRESO A LOS PRODUCTOS
 for producto in productos1:
      Driver.get(producto)
      time.sleep(1)
      nombres1= Driver.find_element(By.XPATH,"//span[@class='vtex-store-components-3-x-productBrand ']").value_of_css_property
      nombres.extend([nombres1])
      time.sleep(1)
      marcas1= Driver.find_element(By.XPATH, "//span[@class='vtex-store-components-3-x-productBrandName']").value_of_css_property
      marcas.extend([marcas1])
      time.sleep(1)

      precios1= Driver.find_element(By.XPATH, "//div[@class='contenedor-precio']//span[1]").value_of_css_property
      if (precios1==False):
            precios1= Driver.find_element(By.XPATH, "//p[@class='discoargentina-store-theme-2HGAKpUDWMGu8a66aeeQ56']").value_of_css_property
      precios.extend([precios1])
      time.sleep(2)
 
 
 productos1, nombres1, marcas1, precios1 = 0,0,0,0

 print(len(productos), "Productos")
 print(len(nombres), "Nombres")
 print(len(marcas), "Marcas")
 print(len(precios), "Precios")

 i += 1












