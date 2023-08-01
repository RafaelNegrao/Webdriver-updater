from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico,options=options)

driver.get("https://www.google.com/")






#...

driver.quit()