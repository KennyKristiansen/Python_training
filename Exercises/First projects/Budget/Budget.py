#! python3
# Budget.py - Downloader forbrug og analyserer disse data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, openpyxl, datetime

# File downloading setting
# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)  # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', r'C:\Users\kenny\Documents\Python projects\Budget')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# Define selenium


os.chdir(r'C:\Users\kenny\Documents\Python projects\Budget')


def login():
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('https://www.portalbank.dk/9124/privat/')
    for filename in os.listdir():
        if filename.endswith('.xlsx'):
            os.unlink(filename)
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "nemid_iframe")))
        time.sleep(2)
        login_user = ActionChains(browser)
        login_user.send_keys('USERNAME_HERE', Keys.TAB, 'PASSWORD_HERE', Keys.ENTER)
        login_user.perform()
    except Exception as exc:
        print(str(exc) + ' Unable to login. Service has been terminated.')
    WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "field_title")))
    kontoer = browser.find_elements_by_class_name('list__anchor')
    konto_antal = int(len(kontoer))
    print('Login successful')
    count = 0
    for i in range(konto_antal):

        kontoer = browser.find_elements_by_class_name('list__anchor')
        konto = kontoer[count]
        count += 1
        if konto.text != 'Konto':
            text = konto.text
            text = (text.splitlines())
            print('Looking up: ' + text[1])
            konto.click()
            time.sleep(1)
            try:
                periode = browser.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[3]/div/account-transactions/account-transactions-view-standard/ui-component-wrapper/div/ng-transclude/section/div/account-transactions-search-basic/section/div/div[1]/div/a')
                periode.click()
                time_period = browser.find_element_by_xpath('//*[@id="ui-select-choices-row-1-6"]')
                time_period.click()
                time.sleep(2)
            except Exception as exc:
                print('Was not able to choose right period.')
            try:
                export_button = browser.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[3]/div/account-transactions/account-transactions-view-standard/ui-component-wrapper/div/div/ui-component-header/ng-transclude/ui-context-menu/div/button')
                export_button.click()
                time.sleep(2)
                export = browser.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[3]/div/account-transactions/account-transactions-view-standard/ui-component-wrapper/div/div/ui-component-header/ng-transclude/ui-context-menu/div/ul/li[6]/a')
                export.click()
                time.sleep(2)
                export = browser.find_element_by_xpath(
                    '/html/body/div[1]/div/div/ui-modal/div/div[3]/ng-transclude/uib-accordion/div[1]/section/ul/li[3]')
                export.click()
                print('Saving file as: ' + text[1])
            except Exception as exc:
                print(exc + 'Could not open export menu.')

            # handle excel-sheet

            time.sleep(5)
            workbook = openpyxl.load_workbook('export.xlsx')
            workbook.save(text[1] + '.xlsx')
            workbook.close()
            time.sleep(1)
            os.unlink('export.xlsx')

            browser.back()
            time.sleep(1)
            browser.back()
            time.sleep(3)

    # browser.close()
    # except Exception as exc:
    # print(str(Exception) + ': Login not found')
    # browser.close()


login()
os.chdir(r'C:\Users\kenny\.PyCharm2018.3\config\scratches\Egne programmer')

from PyQt5 import QtWidgets, uic
app = QtWidgets.QApplication([])
dlg = uic.loadUi('Budget_GUI.ui')

dlg.show() #Opens app
app.exec() #Closing app


#def transaction(date,price,describtion):
