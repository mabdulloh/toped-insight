from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import time

def get_all_comments(driver: WebDriver):
    comments = []
    page_size = find_total_page(driver)
    for i in range(page_size - 1):
        comments.extend(get_comments(driver))
        navigate_next_page(driver)
    print(len(comments))
    return comments

def get_comments(driver: WebDriver) -> []:
    text = []
    elements = driver.find_elements(By.XPATH, ("//span[@data-testid='lblItemUlasan']"))
    for element in elements:
        if check_for_selengkapnya(element.parent):
            print("clicking selengkapnya")
            selengkapnya = element.parent.find_element(By.TAG_NAME, "button")
            selengkapnya.click()
            time.sleep(0.5)
            text.append(element.text)
        else:
            text.append(element.text)
    return text

def find_total_page(driver: WebDriver) -> int:
    element = driver.find_element(By.XPATH, "//nav[@data-testid='btnSelectPage0']")
    pages = element.find_elements(By.TAG_NAME, "li")
    pages_len = len(pages)
    return int(pages[pages_len - 2].text)

def navigate_next_page(driver: WebDriver):
    driver.find_element(By.XPATH, "//button[@aria-label='Laman berikutnya']").click()
    time.sleep(1)

def check_for_selengkapnya(element: WebElement):
    try:
        element.find_elements(By.TAG_NAME, "button")
        return True
    except NoSuchElementException:
        return False