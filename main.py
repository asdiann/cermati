from selenium import webdriver

PATH = "C:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)


#driver.quit()


