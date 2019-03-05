
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# create a new chrome session

driver = webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Temp\\Temp1_chromedriver_win32.zip\\chromedriver.exe")
driver.get("https://www.filedropper.com/")
picture = "C:\\Users\\admin\\Downloads\\IMAGEDOWNLOAD\\image5.jpg"
inputfile=driver.find_element(By.XPATH,'//*[@id="uploadFile"]').send_keys(picture)
#driver.save_screenshot("C:\\Users\\admin\\AppData\\Local\\Temp\\Temp1_chromedriver_win32.zip\\haiamazon.png")
driver.maximize_window()
driver.implicitly_wait(15)
print("The title of the page is :")
print(driver.title)
print("The URL is :")
print(driver.current_url)
driver.implicitly_wait(15)
driver.refresh()

print("SUCESSFULLY RUNNING")
driver.close()