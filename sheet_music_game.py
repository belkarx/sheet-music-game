from selenium import webdriver
import random

driver = webdriver.Firefox()

links = open("sheet_music", 'r').read().split("\n")

#just dont look at the tab names and this should serve its purpose

for link in random.sample(links, 2):
    driver.get(link.split("|||")[1])
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * 0.1);")
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
