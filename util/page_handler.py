from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

def get_comments(driver: WebDriver):
    text = []
    elements = driver.find_elements(By.XPATH, ("//span[@data-testid='lblItemUlasan']"))
    for element in elements:
        text.append(element.text)
    return text