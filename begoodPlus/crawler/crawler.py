from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def init():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver;
    
def login(driver):
    driver.get("https://app.site123.com/manager/wizard.php?w=3809992&from=dash")
    driver.find_element_by_id("username").send_keys("m.s.globalspam@gmail.com")
    driver.find_element_by_id("password").send_keys("MSGLOBAL123")
    driver.find_element_by_id("login-submit").click()

def go_to_all_products(driver):
    driver.find_element_by_id("wizardTab4button").click()
    driver.find_element_by_xpath('//*[@id="card_112"]/div[2]/div[2]/div/div[2]/a/div').click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="moduleSideMenu"]/ul/li[3]/a'))
        )
        driver.find_element_by_xpath('//*[@id="moduleSideMenu"]/ul/li[3]/a').click()
    finally:
        pass
    
    
    
if __name__ == '__main__':
    driver = init()
    login(driver)
    go_to_all_products(driver)
    
    elms = driver.find_element_by_class_name("edit-item-btn")
    print(elms)
    print(elms.length)

while True:
    pass