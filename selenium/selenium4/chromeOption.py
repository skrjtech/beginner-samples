from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--kiosk')
options.add_argument('--lang=ja')

options.add_argument('--user-agent=hogehoge')                                                           # UserAgent

options.add_argument("--headless")                                                                      # バックグラウンド起動
options.add_argument('--disable-gpu')                                                                   # GPUハードウェアアクセラレーションの機能を無効
options.add_argument("--disable-extensions")                                                            #  
options.add_argument('--disable-desktop-notifications')                                                 # 

options.add_argument('--incognito')                                                                     # シークレットモード起動
options.add_argument('--start-maximized')                                                               # 起動時ウィンドウサイズ
options.add_argument('--window-size=1920,1080')                                                         # ウィンドウサイズ指定

options.add_argument('--disable-extensions')                                                            # 拡張機能の無効化
options.add_argument('--no-sandbox')                                                                    # サンドボックスの解除
options.add_argument('--disable-web-security')                                                          # 
options.add_argument('--disable-dev-shm-usage')                                                         # /dev/shmの使用禁止
options.add_argument('--ignore-certificate-errors')                                                     # SSL認証を無効
options.add_argument('--allow-running-insecure-content')                                                

options.add_argument('--user-data-dir=XX')                                                              # ユーザープロファイルの保存先を指定
options.add_argument('--profile-directory=XX')                                                          # 使用するユーザープロファイルを指定

options.add_argument('--proxy-auth=user:pass')                                                          # プロキシーサーバーのユーザー名とパスワードを設定
options.add_argument('--proxy-server=http://0.0.0.0:0000')                                              # プロキシサーバー指定

options.add_argument('--use-fake-ui-for-media-stream')                                                  # カメラ（マイク）ポップアップの無効化 
options.add_argument('--use-fake-device-for-media-stream')                                              # ダミーデバイス カメラとマイクのダミーを用意するオプション
options.add_argument('--blink-settings=imagesEnabled=false')                                            # 画像非表示
options.add_argument('--use-file-for-fake-video-capture=~/video/sample.y4m')                            # ダミーカメラの設定
options.add_argument('--use-file-for-fake-audio-capture=~/audio/sample.wav')                            # ダミーオーディオの設定

options.add_experimental_option('prefs', 'download.default_directory:~/Download')                       # ダウンロードディレクトリの指定
options.add_experimental_option('prefs', "'profile.default_content_setting_values.notifications': 2")   # 通知ポップアップの無効化

options.add_experimental_option('prefs', "'credentials_enable_service': False")                         # パスワード保存のポップアップを無効
options.add_experimental_option('prefs', "'profile.password_manager_enabled': False")                   # パスワード保存のポップアップを無効

service = Service(executable_path=ChromeDriverManager().install())
Driver = webdriver.Chrome(service=service, options=options)

Driver.get('chrome://version')