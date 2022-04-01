from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
from selenium.webdriver.chrome.options import Options
from secrets import user, password 
import time

options = webdriver.ChromeOptions()
 
PATH = 'C://Program Files (x86)//chromedriver.exe'
driver=webdriver.Chrome(PATH, options=options)
 
### login
 
username= user #input("Enter your username: ")
password = password #getpass('Enter your password:')
url='https://www.chessmasterschool.com/'

driver.get(url)
username_textbox = driver.find_element(By.NAME, 'login')
username_textbox.send_keys(username)

password_textbox = driver.find_element(By.NAME, 'parola')
password_textbox.send_keys(password)

login_button = driver.find_element(By.XPATH, '//*[@id="loginform"]/div/form/button')
login_button.submit()

List=[]

## get all links
total=driver.find_elements(By.TAG_NAME,"a")

for x in total:
    a= x.get_attribute("href")
    List.append(a)

url= 'https://www.chessmasterschool.com/clients/program/openingprep.php#clienttop'   
driver.get(url)
file = (driver.find_elements(By.XPATH,"//*[@href]"))
for x in file:
        a= x.get_attribute("href")
        List.append(a)    


for x in range (1, 9):
    url= 'https://www.chessmasterschool.com/clients/program/month0{}.php#clienttop'.format(x)
    driver.get(url)
    file = (driver.find_elements(By.XPATH,"//*[@href]"))
    for x in file:
        a= x.get_attribute("href")
        List.append(a)
    
for x in range (10, 13):             
    url= 'https://www.chessmasterschool.com/clients/program/month0{}.php#clienttop'.format(x)
    driver.get(url)
    file = (driver.find_elements(By.XPATH,"//*[@href]"))
    for x in file:
        a= x.get_attribute("href")
        List.append(a)


print(len(List))
print('\n')
print(List) 
print('\n')

Links=[]

## Download pdfs and videos
for x in List:
    if ('pdf' in str(x)) or ('mp4' in str(x)):
        Links.append(x)
print('\n')
print (len(Links))
print('\n')

Links = list(dict.fromkeys(Links))
print('\n')
print (len(Links))
print('\n')
        
print (Links)        
 

setting=driver.get('chrome://settings/content/pdfDocuments')
time.sleep(5) 


for x in Links:
    driver.get(x)
    time.sleep(2)

 

driver.close()
 
 