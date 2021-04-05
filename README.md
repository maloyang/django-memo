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
    - 其中，'NAME'指的是資料庫的名稱
    ```
    ...

    ALLOWED_HOSTS = ['*']
    #ALLOWED_HOSTS = []

    ...

    DATABASES = {
        'default':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'water',
            'USER': 'username',
            'PASSWORD': 'this-is-my-pwd',
            'HOST': 'myserver.com.tw',
            'PORT': '3306',
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
    
  - 當然這時候就需要安裝mariaDB (or mySQL)的python套件，我之前使用pymysql，但網路上有人建議在django中使用mysqlclient [ref](https://riptutorial.com/django/example/17418/mysql---mariadb)
    - 我先安裝pymysql: `pip install pymysql`
    - but 後面做資料庫遷移時就出錯了....，有提示訊息:
    ```
    django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
    Did you install mysqlclient?
    ```
    - 改安裝mysqlclient: `pip install mysqlclient`

- 資料庫遷移: 在django中本身有自己預設的很多資料表(對應到資料模型)，因此前置作業弄好後，接著就是要來做`資料庫的遷移`(django都是這樣稱呼這個動作的)
- 下指令 (p3-14)
  - `python manage.py makemigrations` 產生需要的SQL程式
  - `python manage.py migrate` 利用makemigrations產生的SQL程式來產生資料表
  - 過程如下:
  ```
  (venv) D:\python\django\water_prj\water>python manage.py makemigrations
  No changes detected

  (venv) D:\python\django\water_prj\water>python manage.py migrate
  System check identified some issues:

  WARNINGS:
  ?: (mysql.W002) MariaDB Strict Mode is not set for database connection 'default'
          HINT: MariaDB's Strict Mode fixes many data integrity problems in MariaDB, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
  Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying sessions.0001_initial... OK
  ```
  - 資料庫如下圖，除了data_table以外，都是django建立的
  - ![img](img/waterdb1.png)

- 這時可以啟動web server，確認我們初步建置沒有問題， `python manage.py runserver` (p3-15)
  - 用: http://localhost:8000 就可以看到網頁
  - 也可以用 `python manage.py runserver 8080` 指定port
  - 或是用 `python manage.py runserver 0:8000` 讓web server可以對任意IP做服務(這邊 0 意指 0.0.0.0)

- 建立water資訊的APP: `python manage.py startapp water_signal`
  - 以此APP來提供所有資料的API
  - 建立新App後，要先在 ./water/settings.py 中登記這一個App，修改如下:
  ```
  INSTALLED_APPS = [
      ...
      'django.contrib.staticfiles',
      'water_signal',
  ]  
  ```
  - 接著要建立MTV中的View -> 也就是MVC中的controller這部分，做為商業邏輯的功能 (App中的views.py檔案)
  - 先建立一個 Hello IoT!的API，修改views.py程式如下
  ```
  from django.shortcuts import render
  from django.http import HttpResponse

  # Create your views here.
  def web_hello_iot(request):
      return HttpResponse('Hello IoT')  
  ```
  - URL mapping的規劃，假設 ~/hello 是我們要規劃的網址，修改./water/urls.py 如下:
  ```
  from django.contrib import admin
  from django.urls import path, include, re_path
  from water_signal import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('water_signal/', include('water_signal.urls', namespace='water_signal')),
  ]
  ```
  - 其中第一行 path('admin/'.... --> 是指 ~/admin/ 網址要進到admin管理頁面去
  - 新加入的 path('hello/'.... --> 是指 ~/hello/ 網址要用 water_iot 模組中的urls.py去進一步解析
  - 所以這邊我們在新增一個urls.py在water_iot的App資料夾下，內容如下
  ```
  from django.urls import path
  from water_signal import views

  app_name = 'water_signal'

  urlpatterns = [
      path('',  views.web_hello_iot, name='water_signal'), #讓views.py中的web_hello_iot函式處理
  ]  
  ```
  - 以上結束後，用 `http://localhost:8000/water_signal/` 就可以看到我們剛剛完成的網頁 `Hello IoT`

----

- 進一步了解 `water/urls.py`, `water_signal/urls.py` 各自的功能區分，再做個實驗，我們在 `water/signal/urls.py`中加入新的path

```
from django.urls import path
from water_signal import views

app_name = 'water_signal'

urlpatterns = [
    path('',  views.web_hello_iot, name='water_signal'), #讓views.py中的web_hello_iot函式處理
    path('hello2',  views.web_hello2),
]
```

- 然後在 water_signal/views.py 加入新的function (web_hello2)，如下:
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def web_hello_iot(request):
    return HttpResponse('Hello IoT')

def web_hello2(request):
    return HttpResponse('Hello2')
```

- 執行程式 `python manage.py runserver`，就可以看到我們新增的網頁 `http://localhost:8000/water_signal/hello2`
- 由此可知，`water/urls.py`, `water_signal/urls.py` 這兩個的path設計是互相疊加的效果

----

- 在進一步測試，加入hello3的path，這一次我們要測試的試HttpResponse()這一個函式
- 在`water_signal/views.py`中加入

```
def web_hello3(request):
    html = '''
    <!doctype html>
    <html>
    <head>
    <title>水文IoT</title>
    <meta charset='utf-8'>
    </head>

    <body>
    <p>這是水文IoT的網頁</p>
    </body>
    </html>
    '''
    return HttpResponse(html)
```
- 並修改 `water_signal/urls.py`如下

```
from django.urls import path
from water_signal import views

app_name = 'water_signal'

urlpatterns = [
    path('',  views.web_hello_iot, name='water_signal'), #讓views.py中的web_hello_iot函式處理
    path('hello2',  views.web_hello2),
    path('hello3',  views.web_hello3),
]
```

- 執行程式 `python manage.py runserver`，就可以看到我們新增的網頁 `http://localhost:8000/water_signal/hello2`
- 可以得知 HttpResponse()只是原原本本的把我們的字串回傳 --> 那為何還要他呢?

