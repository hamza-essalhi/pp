# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from seleniumwire import webdriver
import random
import keyboard
from datetime import datetime
t=datetime.now().strftime('%H:%M:%S')

print(t)
proxyList=[]
file= open('Webshare 100 proxies.txt','r')
data=file.read()
proxyList=data.split("\n")
def loadRandomProxy():
    proxy=random.choice(proxyList)
    n=proxy.split(':')
    return n

# users=int(input('daKhel ch7al mn user mn 1 tal 10 :'))
# lwa9t=int(input('dkahl ch7al bghiti dial lwa9t bd9ay9 :'))
users=5
def script():
    
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("window-size=1500,1000")
    for x in range(0, users):
        config=loadRandomProxy()
        print('proxy :',config)
        proxy=config[0]
        port=config[1]
        user=config[2]
        password=config[3]
        options_seleniumWire = {
        'proxy': {
            'https': f'http://{user}:{password}@{proxy}:{port}',
        }
        }
        
        globals()['driver%s' % x]  = webdriver.Chrome ( options=chrome_options, seleniumwire_options=options_seleniumWire)
        globals()['driver%s' % x].get('https://www.youtube.com/@Castor99')
        time.sleep(3)
        try:
            globals()['driver%s' % x].find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button').click()
            time.sleep(3)
        except:
            pass
        v=globals()['driver%s' % x].find_element(By.CLASS_NAME,'ytd-channel-name').text
        nam=globals()['driver%s' % x].find_element(By.ID,'subscriber-count').text 
        print(v,nam)
        time.sleep(3)
        
            
      
  
    hrefs = [video.get_attribute('href') for video in driver0.find_elements(By.ID,'thumbnail')]
    for i in hrefs:
        try:
            for x in range(0,users):
                globals()['driver%s' % x].execute_script("window.open('');")
                globals()['driver%s' % x].switch_to.window(globals()['driver%s' % x].window_handles[1])
                globals()['driver%s' % x].get(i)
            time.sleep(random.randint(10,20))
            for x in range(0,users):
                globals()['driver%s' % x].close()
                globals()['driver%s' % x].switch_to.window( globals()['driver%s' % x].window_handles[0])
        except:
            pass
    for x in range(0,users):
        globals()['driver%s' % x].quit()

while True:
    script()
    if keyboard.is_pressed('q'):
        break