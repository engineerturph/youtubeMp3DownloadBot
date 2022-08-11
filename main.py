from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from waiting import wait, TimeoutExpired
from time import sleep
def downloadFromLınk(link):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.y2mate.com/tr265/youtube-mp3')
    field = driver.find_element(By.ID, 'txt-url')
    field.send_keys('https://www.youtube.com/watch?v=VpwOAEJKB5s')
    button = driver.find_element(By.ID, 'btn-submit')
    button.click()
    def waitButton2():
        try:
            print('button2')
            button2 = driver.find_element(By.ID, 'process_mp3')
            button2.click()
        except:
            sleep(1)
            waitButton2()
    waitButton2()

    def waitButton3():
        try:

            button3 = driver.find_elements(By.CLASS_NAME,  "btn-success")
            print('button3',button3)
            button3[2].click()
        except:
            sleep(1)
            waitButton3()
            return 1
    waitButton3()

    while(True):
        pass
downloadFromLınk(1)

