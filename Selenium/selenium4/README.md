# Selenium4 Docs
詳しいことはリンク先から [![Selenium Docs](http://www.w3.org/2000/svg)](https://www.selenium.dev/ja/documentation/overview/components) 

# Selenium4 Install
## pip
```
pip install selenium
```
## conda
```
conda install -c conda-forge selenium
```
## source
```
git clone https://github.com/SeleniumHQ/selenium.git
cd selenium/py
python setup.py install
```
# Selenium4 アップグレード
## python 3.7 <= 3.X
```
pip install selenium==4.4.3
```
# Selenium4 Usage
## WebDriver Import
```
from selenium import webdriver

Driver = webdriver.Chrome()

Driver.get("http://selenium.dev")

Driver.quit()
```
# Selenium4 Web Driver Install 
様々なドライバーに適したサンプル: [Webdriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager)
## WebDriver Manager Install
```
pip install webdriver-manager
```
```
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
Driver = webdriver.Chrome(service=service)

Driver.quit()
```
## 手動でウェブドライバーのインストール
|Browser|Supported OS|Maintained by|Download|Issue Tracker|
|:---|:---|:---|:---|:---|
|Chromium/Chrome|Windows / macOS / Linux|Google|[Downloads](https://chromedriver.chromium.org/downloads)|[Issues](https://bugs.chromium.org/p/chromedriver/issues/list)|
|Firefox|Windows / macOS / Linux|Mozilla|[Downloads](https://github.com/mozilla/geckodriver/releases)|[Issues](https://github.com/mozilla/geckodriver/issues)|
|Edge|Windows / macOS|Microsoft|[Downloads](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver)|[Issues](https://github.com/MicrosoftEdge/EdgeWebDriver/issues)|
|Internet Explorer|Windows|Selenium Project|[Downloads](https://www.selenium.dev/downloads)|[Issues](https://github.com/SeleniumHQ/selenium/labels/D-IE)|
|Safari|macOS High Sierra and newer|Apple|Built in|[Issues](https://bugreport.apple.com/logon)|
```
cd /opt
sudo mkdir -p WebDriver/bin
sudo chmod a+x -R WebDriver
cd WebDriver/bin
# Chromium/Chrome Download
# 現時点 (2022-09-1) 105.0.5195.52
wget https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
# PATH 追加
export PATH=$PATH:/opt/WebDriver/bin >> ~/.profile
```
## フルパスでWebDriver指定 (Chromium/Chrome)
```
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/opt/WebDriver/bin/chromedriver")
Driver = webdriver.Chrome(service=service)

Driver.quit()
```
## Import Driver
```
from time import sleep as Sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/opt/WebDriver/bin/chromedriver")
Driver = webdriver.Chrome(service=service)

Driver.quit()
```
## リンク検索
```
Driver.get("https://www.google.com")
```
## リンク先のタイトル取得
```
title = Driver.title
```
## 暗黙的な待機 
```
Driver.implicitly_wait(0.5) # 0.5秒待機
```
明示的・暗黙的な待機については, [examples/selenium_wait_or_sleep.py](./examples/selenium_wait_or_sleep.py) で詳しく解説している
## 要素の検索
```
from selenium.webdriver.common.by import By

text_box = Driver.find_element(by=By.NAME, value="val")
submit_button = Driver.find_element(by=By.CSS_SELECTOR, value="val")
```
## 値入力
```
text_box.send_keys("val")
```
## クリック
```
submit_button.click()
```
## 要素のテキストを取得
例) HTML
```
<p id='message'>Hello World!</p>
out: Hello World!
```
```
message = driver.find_element(by=By.ID, value="message")
value = message.text # <- Hello World!
```
## 終了動作
```
Driver.quit()
```
# ブラウザーナビゲーション
```
Driver.get("https://www.google.com")
```
## 前ページ移動
```
Driver.back()
```
## 次ページ移動 ？
```
Driver.navigate().forward();
```
## ページの更新
```
Driver.refresh()
```
# Cookies Usage
## Cookie Add
```
from selenium import webdriver

Driver = webdriver.Chrome()
Driver.get("http://www.example.com")
Driver.add_cookie({"name": "key", "value": "value"})
```
## Get Cookie
```
from selenium import webdriver

Driver = webdriver.Chrome()
Driver.get("http://www.example.com")
Driver.add_cookie({"name": "foo", "value": "bar"})
print(Driver.get_cookie("foo"))
```
## Get Cookies
```
from selenium import webdriver

Driver = webdriver.Chrome()
Driver.get("http://www.example.com")
Driver.add_cookie({"name": "test1", "value": "cookie1"})
Driver.add_cookie({"name": "test2", "value": "cookie2"})
print(Driver.get_cookies())
```
## Cookie Delete
```
from selenium import webdriver
Driver = webdriver.Chrome()

Driver.get("http://www.example.com")
Driver.add_cookie({"name": "test1", "value": "cookie1"})
Driver.add_cookie({"name": "test2", "value": "cookie2"})

Driver.delete_cookie("test1")
```
## Cookie All Delete
```
from selenium import webdriver
Driver = webdriver.Chrome()

Driver.get("http://www.example.com")
Driver.add_cookie({"name": "test1", "value": "cookie1"})
Driver.add_cookie({"name": "test2", "value": "cookie2"})

Driver.delete_all_cookies()
  
```
# 保存ファイルから開く
```
Driver.navigate("file:///index.html")
```