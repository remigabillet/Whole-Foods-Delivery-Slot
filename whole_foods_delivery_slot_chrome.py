import bs4

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


import sys
import time
import os
import random


from datetime import datetime


def log(msg):
   now = datetime.now().strftime("%H:%M:%S")
   print(f"{now} | {msg}")


def sleep_countdown(total_seconds):
   seconds_left = total_seconds
   log(f"Sleep for {seconds_left} seconds ...")
   while seconds_left > 0:
      time.sleep(1)
      seconds_left -= 1

def slots_are_open():
   log(' ************* SLOTS OPEN **************')
   os.system('say "Slots for delivery opened!"')


def getWFSlot(productUrl):
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
   }


   driver = webdriver.Chrome(ChromeDriverManager().install())

   # driver = webdriver.Chrome()
   driver.get(productUrl)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)

   log("Script started.")
   sleep_countdown(45)
   no_open_slots = True


   while no_open_slots:
      # log("Refreshing..")
      driver.refresh()

      page = driver.current_url

      if 'buy/shipoptionselect' in page:
         page = 'shipoptionselect'
      else:
         os.system('say "on the wrong page"')

      log('')
      log(f'Refreshed {page}')

      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      
      # METHOD 1
      element = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal')
      if element and 'Next available' in element.text:
         slots_are_open()
         continue

      # METHOD 2
      all_dates = soup.findAll("div", {"class": "ufss-date-select-toggle-text-availability"})
      for each_date in all_dates:
         if "Not available" not in each_date.text:
            slots_are_open()
            continue

      log("NO SLOTS :(")
      
      sleep_countdown(random.randrange(2)+7)


getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


