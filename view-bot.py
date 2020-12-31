### view-bot.py ###
import time
import random
from selenium import webdriver
from links import links

link_count = len(links)

driver = webdriver.Firefox()

link = random.sample(links, 1)[0]
print(link)

views = 10000
for i in range(views):
    time.sleep(10)
    link = random.sample(links, 1)[0]
    driver.get(link)
    print(f'{i} - {driver.title}')
