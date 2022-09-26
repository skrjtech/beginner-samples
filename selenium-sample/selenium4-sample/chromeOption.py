from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--kiosk')
options.add_argument('--lang=ja')
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--noerrdialogs')
options.add_argument('--user-data-dir=XX') # ユーザープロファイルの保存先を指定
options.add_argument('--disable-infobars')
options.add_argument('--start-fullscreen')
options.add_argument('--disable-translate')
options.add_argument('--window-position=0,0')
options.add_argument('--profile-directory=XX') # 使用するユーザープロファイルを指定
options.add_argument('--window-size=1920,1080')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-features=TranslateUI')
options.add_argument('--disable-desktop-notifications')
options.add_argument('--allow-running-insecure-content')

service = Service(executable_path=ChromeDriverManager().install())
Driver = webdriver.Chrome(service=service, options=options, desired_capabilities=desired)

Driver.get('chrome://version')