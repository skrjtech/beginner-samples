# Selenium4 学習用
[![Selenium Docs](http://www.w3.org/2000/svg)](https://www.selenium.dev/ja/documentation/overview/components)
## Selenium4 Install
### conda
```
conda install -c conda-forge selenium
```
### pip
```
pip install selenium
```
### Source
```
git clone https://github.com/SeleniumHQ/selenium.git
cd selenium/py
python setup.py install
```
## Selenium4 へのアップグレード
### python 3.7 <= 3.X
```
pip install selenium==4.4.3
```
# 単純な操作
## ウェブドライバー
```
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()
```
## ドライバーのインストール
様々なドライバーに適したサンプル: [Webdriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager)
### webdriver-managerのインストール
```
pip install webdriver-manager
```
```
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.quit()
```
### 手動でウェブドライバーのインストール
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
### フルパスでWebDriverの指定 (Chromium/Chrome)
```
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/opt/WebDriver/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.quit()
```
# 初歩的な使い方
## セッションの起動
```
from time import sleep as Sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/opt/WebDriver/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.quit()
```
## 情報の取得
```
driver.get("https://www.google.com")
```
## タイトルの取得
```
title = driver.title
```
## 要素が見つかるまで待機
### implicitly_wait
```
driver.implicitly_wait(0.5) # 0.5秒待機
```
## 要素の検索
```
from selenium.webdriver.common.by import By

text_box = driver.find_element(by=By.NAME, value="val")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="val")
```

## クリック
```
# 検索した要素の中に、例えばユーザー名を入力するテキストボックスに入力を送信する事ができる
text_box.send_keys("val")
submit_button.click()
```
## 取得した要素をリクエスト
```
message = driver.find_element(by=By.ID, value="message")
value = message.text
```
## 終了動作
```
driver.quit()
```
# ブラウザーナビゲーション
## ナビゲート
```
driver.get("https://www.google.com")
```
## 戻る動作
```
driver.back()
```
## 移行動作
```
driver.navigate().forward();
```
## 更新動作
```
driver.refresh()
```
# Cookiesの使用方法
## Cookieの追加
```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")
driver.add_cookie({"name": "key", "value": "value"})
```
## 追加したCookieの取得
```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")
driver.add_cookie({"name": "foo", "value": "bar"})
print(driver.get_cookie("foo"))
```
## Cookieの全情報の取得
```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})
print(driver.get_cookies())
```
## Cookiesの削除
```
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

driver.delete_cookie("test1")
```
## Cookiesの全削除
```
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

driver.delete_all_cookies()
  
```
# ファイルからの情報取得
```
driver.navigate("file:///index.html")
```