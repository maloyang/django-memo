# django-memo

- 一開始是由itheme上學習，不過因為過於破碎，吸收的不是太好，且有些指令有遺漏，常常做到一半就做不下去....
- 2020年買入唐元亮老師的[【Django3-從平凡到超凡】](https://www.books.com.tw/products/0010854217?loc=M_0009_006)這本書，感覺有系統多了! 雖然裡面教的並不是我想要的前後端分離，但依然建立了不錯的實作練習 (每個人喜愛的書寫風格不同，但至少我是收穫良多)

## django project指令memo

- 我是在資料夾`D:\python\django\water_prj`中開始我的專案的
- virtualenv環境建立: (p3-2)
  - `D:\python\django\water_prj>virtualenv venv`
  - `venv\Scripts\activate.bat` 啟用 venv環境

- 安裝django環境 (p3-3)
  - `pip install django`
  - 確認目前安裝的套件:
  ```
  (venv) D:\python\django\water_prj>pip freeze
  asgiref==3.3.1
  Django==3.1.7
  pytz==2021.1
  sqlparse==0.4.1  
  ```
  
- 建立新專案 (p3-6)
  - `django-admin startproject water`
  - 用 tree 指令看一下目前django為我們產生的專案基本架構 `tree D:\python\django\water_prj\water /F /A`
  ```
  D:\PYTHON\DJANGO\WATER_PRJ\WATER
  |   manage.py
  |
  \---water
          asgi.py
          settings.py
          urls.py
          wsgi.py
          __init__.py  
  ```
  - 在專案資料夾`water`中會建立另一個water資料夾，是專案直屬的App (djangoe是這樣稱呼的)，我們可以在一個專案中建立多個App，每一個有不同的功能，達成模組化管理
  - manage.py則是Django的專案管理程式
  - `water` App中的檔案說明如下:
    - __init__.py : 設定此目錄為Python package
    - asgi.py : 非同步伺服器閘道介面 (Asynchronous web server gateway interface)，django好像都用這個
    - settings.py : 專案設定擋 (資料庫的資訊設定在這邊)
    - urls.py : 專案的 URL request 設定擋
    - wsgi.py : 伺服器閘道介面 (web server gateway interface)，
  - 編輯設定擋
    - 改host, db setting, lang., time_zone
    ```
    ...

    ALLOWED_HOSTS = ['*']
    #ALLOWED_HOSTS = []

    ...

    DATABASES = {
        'default':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blog',
            'USER': 'user',
            'PASSWORD': 'ixdezuser',
            'HOST': 'dosg.maria.ewxew.com',
            'PORT': '43306',
        }
    }
    ''' # default DB setting
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    '''

    ...

    LANGUAGE_CODE = 'zh-hant'
    #LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'Asia/Taipei'
    #TIME_ZONE = 'UTC'

    ```
    
