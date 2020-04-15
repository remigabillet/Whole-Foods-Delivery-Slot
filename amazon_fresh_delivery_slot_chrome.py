import bs4

from selenium import webdriver

import sys
import time
import os


def getWFSlot(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    driver = webdriver.Chrome()
    driver.get(productUrl)           
    html = driver.page_source
    soup = bs4.BeautifulSoup(html)
    time.sleep(60)
    duration = 5
    no_open_slots = True

#    while no_open_slots:
#       driver.refresh()
#       print("refreshed")
#       html = driver.page_source
#       soup = bs4.BeautifulSoup(html)
#       time.sleep(2)

#       no_open_slots = "No doorstep delivery windows are available for"
#       try:
#          no_slots_from_web = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/form/div[3]/div[4]/div/div[2]/div[2]/div[6]/div/div[2]/div/div[2]/div/div[20]/div[1]/div[1]/div/div/div/span').text
#          if no_open_slots in no_slots_from_web:
#             continue
#          else:
#             print('SLOTS OPEN!')
#             os.system('say "Slots for delivery opened!"')
#             no_open_slots = False
#             time.sleep(1400)
#       except AttributeError:
#          print('SLOTS OPEN!')
#          os.system('say "Slots for delivery opened!"')
#          no_open_slots = False
#          time.sleep(1400)


#       try:
#          open_slots = soup.find('div', class_ ='orderSlotExists').text()
#          if open_slots != "false":
#             print('SLOTS OPEN!')
#             os.system('say "Slots for delivery opened!"')
#             no_open_slots = False
#             time.sleep(1400)
#       except AttributeError:
#          continue

    while True:
        if no_open_slots:
            print("Refreshing")
            driver.refresh()
            html = driver.page_source
            soup = bs4.BeautifulSoup(html, 'html.parser')

            # soup.find_all('div', class_='ServiceType-slot-container')[0].find('span', class_="a-size-base-plus").string.strip()
            try:
                # soup.find_all('button', id=re.compile('date-button-'))
                # for day_button in soup.find_all('div', class_='ufss-date-select-toggle-text-container'):
                for slot in soup.find_all('div', class_='ServiceType-slot-container'):
                    # print(f"day button: {day_button}")
                    for availability in slot.find('span', class_="a-size-base-plus"):
                        availability = availability.string.strip()
                        print(f"availability: {availability}")
                        # for status in availability.stripped_strings:
                        #     print(f"status: {status}")
                        if status != 'Not available':
                            print('SLOTS OPEN!')
                            os.system('say "Slots for delivery opened!"')
                            no_open_slots = False
                if no_open_slots:
                    sys.stdout.write('\rRefreshed at {}.'.format(time.strftime('%H:%M:%S', time.localtime())))
                    sys.stdout.flush()
                    time.sleep(duration)
            except AttributeError as error:
                print('error: {0}'.format(error))
                continue
        else:
            time.sleep(duration)
      

getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


