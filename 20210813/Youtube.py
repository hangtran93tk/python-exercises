import webbrowser
import time
import sys
import os

try:
    while True:
        webbrowser.open("https://www.youtube.com/watch?v=G5MyiQQCmPA&t=12s")
        time.sleep(300)
        os.system("taskkill /im chrome.exe /f")
        # os.system("pkill -f 'PATTERN'")
        webbrowser.open("https://www.youtube.com/watch?v=v_pnqbfAoYw&t=9s")
        time.sleep(300)
        os.system("taskkill /im chrome.exe /f")
        # os.system("pkill -f 'PATTERN'")
except KeyboardInterrupt as e:
    sys.exit()

# from selenium import webdriver
# from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://m.youtube.com/watch?v=G5MyiQQCmPA&list=PLIEkkiNDdc--WAuWctsnPJL00PnBnBOIc&index=1")
# sleep(10)
# driver.close()
