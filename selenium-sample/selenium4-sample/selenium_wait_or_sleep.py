#/user/bin/env python
# -*- coding: utf-8 -*-

"""
-> 暗黙的・明示的な待機
    -> 明示的
        -> WebDriverWait 指定の要素が読み込まれるまで待機
            ->  expected_conditions
        -> time.sleep 指定の要素の確認なしで強制的に待機
    -> 暗黙的
        -> implicitly_wait 指定時間までに全要素が読み込まれなかったらタイムアウト
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager

"""
-> expected_conditions:
    -> visibility_of_element_located	    指定した要素の表示される
    -> text_to_be_present_in_element	    指定したテキストが表示される
    -> presence_of_all_elements_located	    ページ内のすべての要素が読み込まれる
    -> presence_of_element_located	        DOM要素内に指定した要素が現れる
    -> alert_is_present	                    Alertが表示される
    -> element_to_be_clickable	            要素がクリック出来る状態になる
"""

options = webdriver.ChromeOptions()
desired = DesiredCapabilities.CHROME

service = Service(executable_path=ChromeDriverManager().install())
Driver = webdriver.Chrome(service=service, options=options, desired_capabilities=desired)
# 明示的な待機
Wait = WebDriverWait(Driver, 60) # 待機時間条件定義 60秒

url = "https://www.google.com/"
Driver.get(url)
# Load Wait
Element = Wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "selector")
    )
)
# Search Key
Element.send_keys("keyword")
Element.submit() # Search Run
# Load Wait
Element = Wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "selector")
    )
)
# Run Many code
"""
Driver.find_element(By.CSS_SELECTOR, "selector").clear()
Driver.find_element(By.CSS_SELECTOR, "selector").send_keys()
# 明示的な待機後にクリック
time.sleep(3); Driver.find_element(By.CSS_SELECTOR, "selector").click()
"""

# 暗黙的な待機
Driver.get(url)
Driver.implicitly_wait(60)
"""
Driver.find_element(By.CSS_SELECTOR, "selector").clear()
Driver.find_element(By.CSS_SELECTOR, "selector").send_keys()
# 明示的な待機後にクリック
time.sleep(3); Driver.find_element(By.CSS_SELECTOR, "selector").click()
"""
