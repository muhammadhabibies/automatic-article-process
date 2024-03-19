from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Mendapatkan direktori kerja saat ini
import os
current_directory = os.getcwd()
path = os.path.join(current_directory, 'index.html')

# make a variable call web

web = webdriver.Chrome()
# path = "https://www.editor.promediaindonesia.com"
web.get(path)

# time.sleep(10)

username = 'iboncc88@gmail.com'
password = '123'
title = 'Ini adalah judul yang telah diinputkan'

# login
WebDriverWait(web, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/form/fieldset/p[1]/input"))).send_keys(username)
WebDriverWait(web, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/form/fieldset/p[2]/input"))).send_keys(password)

# element = web.find_element_by_id('select_section')
# drp = Select(element)
# drp.select_by_visible_text('Budha')
Select(web.find_element(By.TAG_NAME, "select")).select_by_index(4)

# navbar
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/aside/section/ul/li[2]/a"))).click()
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a"))).click()

# title
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div[1]/section/div[1]/div[2]/div[1]/div/div[1]/input[4]"))).send_keys(title)
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div[1]/section/div[1]/div[2]/div[2]/div/div[1]/span/span[1]/span/span[1]"))).click()
rubrik = 'Teknologi'
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/span/span/span[1]/input"))).send_keys(rubrik)
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/span/span/span[1]/input"))).send_keys(Keys.RETURN)
author = 'Muhammad Habibie Syihab'
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div[1]/section/div[1]/div[2]/div[2]/div/div[5]/span/span[1]/span/ul/li[1]/span"))).click()
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div[1]/section/div[1]/div[2]/div[2]/div/div[2]/textarea"))).click()
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div[1]/section/div[1]/div[2]/div[2]/div/div[5]/span/span[1]/span/ul/li/input"))).send_keys(author)
time.sleep(1)
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div[1]/section/div[1]/div[2]/div[2]/div/div[5]/span/span[1]/span/ul/li/input"))).send_keys(Keys.RETURN)

# Related
WebDriverWait(web, 120).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div[1]/section/div[1]/div[2]/div[1]/div/div[3]/button"))).click()
time.sleep(2)
# keyyy = 'ayam goreng'
# WebDriverWait(web, 120).until(EC.element_to_be_clickable(
#     (By.ID, "general-modal"))).send_keys(keyyy)

# drp.select_by_index(4)
# drp.select_by_value("budha")
# WebDriverWait(web, 120).until(EC.element_to_be_clickable(
#     (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/button/span"))).click()
