from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=webdriver.ChromeOptions()
    )
    driver.implicitly_wait(10)

    driver.get("https://www.google.com/doodles?hl=ja")

    print(driver.find_element(By.ID, "latest-title").text)
    driver.quit()
