from base.baseControl import BaseControl
import util.settings as settings
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\Administrator\Desktop\UIAutoFrameWork\driver\chromedriver.exe")

# driver.get("http://192.168.1.180:9527")
# sleep(5)
# driver.quit()

base = BaseControl(driver)

base.open_url()
sleep(5)
driver.quit()
