
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as ec
import os
import time
import keyboard


class xboxaplicationsTest():
    
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
    
    
    def openbrowserandurl(self):
        self.driver.maximize_window()
        self.driver.get('https://www.microsoft.com/es-mx/')

        #Click on 'Windows' link
        ui.WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#shellmenu_2')))
        self.driver.find_element(by=By.CSS_SELECTOR,value='#shellmenu_2').click()
        ui.WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#search')))
        
        #Click on 'search' image
        self.driver.find_element(by=By.CSS_SELECTOR,value='#search').click()
        time.sleep(2)
        
        #Set the text 'Xbox' in searching bar
        self.driver.find_element(by=By.CSS_SELECTOR,value= '#cli_shellHeaderSearchInput').send_keys('Xbox')
        self.driver.find_element(by=By.CSS_SELECTOR,value='#search').click()
        
        #Handle a change of country market pop up and keep the MX market
        try:
            self.driver.find_element(by=By.CSS_SELECTOR,value='#R1MarketRedirect-close').click()
            time.sleep(2)
        except:
            print('It will keep in MX webpage')
        
        #Click on 'buying' link
        self.driver.find_element(by=By.CSS_SELECTOR,value='#coreui-pivotheader-s3sdtmy > div > div > header > a:nth-child(1)').click()
        ui.WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#refine-by-menu-title-Categorías > div > ul > li:nth-child(1) > a')))
        
        #Click on 'Applications' link 
        self.driver.find_element(by=By.CSS_SELECTOR,value='#refine-by-menu-title-Categorías > div > ul > li:nth-child(1) > a').click()
        ui.WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#coreui-productplacementlist-1g76zxk > div:nth-child(3) > div')))
        time.sleep(2)
        
        #store items in page 1
        elements = self.driver.find_element(by=By.CSS_SELECTOR,value='#coreui-productplacementlist-1g76zxk > div:nth-child(3) > div')
        i = 0
        titles = []
        for allitmes in elements.find_elements(by = By.XPATH,value = '//*') :
            i+=1
            titles.append(allitmes)
        a = i/90
        print(f'There are {i/a:.0f} elements in the first page')
        #print(titles)
        time.sleep(3)
        
        #store items in page 2
        self.driver.find_element(by=By.CSS_SELECTOR,value= '#coreui-productplacementlist-1g76zxk > div:nth-child(3) > ul > li:nth-child(3) > a').click()
        elements = self.driver.find_element(by=By.CSS_SELECTOR,value='#coreui-productplacementlist-1g76zxk > div:nth-child(3) > div')
        i = 0
        titles = []
        for allitmes in elements.find_elements(by = By.XPATH,value = '//*') :
            i+=1
            titles.append(allitmes)
        a = i/90
        print(f'There are {i/a:.0f} elements in the second page')
        #print(titles)
        time.sleep(3)
        
        #store items in page 3
        self.driver.find_element(by=By.CSS_SELECTOR,value= '#coreui-productplacementlist-1g76zxk > div:nth-child(3) > ul > li:nth-child(4) > a').click()
        elements = self.driver.find_element(by=By.CSS_SELECTOR,value='#coreui-productplacementlist-1g76zxk > div:nth-child(3) > div')
        i = 0
        titles = []
        for allitmes in elements.find_elements(by = By.XPATH,value = '//*') :
            i+=1
            titles.append(allitmes)
        a = i/90
        print(f'There are {i/a:.0f} elements in the third page')
        #print(titles)
        time.sleep(3)

        #Back into page 1 and finds the first NON-FREE item, and selects it
        self.driver.find_element(by=By.CSS_SELECTOR,value= '#coreui-productplacementlist-1g76zxk > div:nth-child(3) > ul > li:nth-child(2) > a').click()
        elements = self.driver.find_element(by=By.CSS_SELECTOR,value='#coreui-productplacementlist-1g76zxk > div:nth-child(3) > div')
        i = 0
        titles = []
        for allitmes in elements.find_elements(by = By.PARTIAL_LINK_TEXT,value = 'MXN') :
            titles.append(allitmes)
        element = titles[0]
        element.click()
        time.sleep(5)
        
        #Handle Registering pop up and close it
        try:
            self.driver.find_element(by=By.CSS_SELECTOR,value='#email-newsletter-dialog > div.sfw-dialog > div.c-glyph.glyph-cancel').click()
            time.sleep(2)
        except:
            print('Registering pop up got closed')
        
        #Click on 3 dot button and add the item to the shopping cart 
        elements = self.driver.find_element(by=By.CSS_SELECTOR,value= '#ButtonPanel_buttonPanel_OverflowMenuTrigger')
        self.driver.find_element(by=By.CSS_SELECTOR,value= '#ButtonPanel_buttonPanel_OverflowMenuTrigger').click()
        keyboard.send('tab')
        keyboard.send('tab')
        keyboard.send('enter')
        time.sleep(5)

        #Open the shopping cart and eliminate the item
        ui.WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#store-cart-root > div > div > div > section.main--klSNnr0K > div > div > div > div > div > div.itemDetailsAndLegal--ULuWkT5t > div.item-details > div.item-quantity-price > div.item-quantity > div > div:nth-child(2)')))
        element = self.driver.find_element(by = By.CSS_SELECTOR,value ='#store-cart-root > div > div > div > section.main--klSNnr0K > div > div > div > div > div > div.itemDetailsAndLegal--ULuWkT5t > div.item-details > div.item-quantity-price > div.item-quantity > div > div:nth-child(2)')
        print(f'You have {element.text} element in the shopping cart')
        time.sleep(5)
        self.driver.find_element(by= By.CSS_SELECTOR,value= '#store-cart-root > div > div > div > section.main--klSNnr0K > div > div > div > div > div > div.itemDetailsAndLegal--ULuWkT5t > div.legalAndStatementContainer--dz8EQOG7 > div > button:nth-child(1)').click()
        ui.WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#store-cart-root > div > div > div > section.main--klSNnr0K > p')))
        element = self.driver.find_element(by= By.CSS_SELECTOR,value= '#store-cart-root > div > div > div > section.main--klSNnr0K > p')
        print(f'Spanish message after erase the item in the shopping cart: "{element.text}"')


if __name__ == "__main__":
    obj = xboxaplicationsTest()
    obj.openbrowserandurl()
