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
- 我們把 HttpResponse拿掉，只把 html 變數內容回傳，就變成 error 產生了，django無法處理GET回應，所以這應該是Django中處理http回應需要有的function包裝(如對GET, POST的標籤註記)，不使用HttpResponse()函數會讓Django不知道如何工作

----

## 管理者介面 (p8-9)

- 前面實做過程中，會注意到 `water/urls.py`中的這一個path `path('admin/', admin.site.urls),`，這是Django內建的管理者功能 --> 用Django的價值就在這邊體現!
- 首先， `python manage.py createsuperuser`
- 這邊我們先以admin, wb@12345678建立
```
(venv) D:\python\django\water_prj\water>python manage.py createsuperuser
使用者名稱 (leave blank to use 'malo'): wbadmin
電子信箱:
Password:
Password (again):
Superuser created successfully.
```
- 做到這邊就可以由 `http://localhost:8000/admin/` 連結進入管理頁面了

----
## 加入資料庫的連結

- 要在管理者介面中可以管理我們的資料，這時就要建立model，修改`water_signal/models.py`
```
from django.db import models

# Create your models here.
class Water_data(models.Model):
    data_time = models.DateField()
    water_level1 = models.FloatField()
    water_level2 = models.FloatField()

    def __str__(self):
        return '[%s] %s, %s' %(self.data_time, self.water_level1, self.water_level2)
```

- 再執行 `python manage.py makemigrations`，會產生相對應需要的SQL指令於`water_signal/migrations/0001_inital.py`
```
(venv) D:\python\django\water_prj\water>python manage.py makemigrations
Migrations for 'water_signal':
  water_signal\migrations\0001_initial.py
    - Create model Water_data
```
- 執行migrate的指令
```
(venv) D:\python\django\water_prj\water>python manage.py migrate
System check identified some issues:

WARNINGS:
?: (mysql.W002) MariaDB Strict Mode is not set for database connection 'default'
        HINT: MariaDB's Strict Mode fixes many data integrity problems in MariaDB, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, water_signal
Running migrations:
  Applying water_signal.0001_initial... OK
```

- 至此，執行`python manage.py runserver`，就可以再開始使用admin去管理資料了?! --> no~no~ 要可以在管理者介面看到資料，還要登記再 water_signal/admin.py 中才行! 如下:
```
from django.contrib import admin
from water_signal.models import Water_data

# Register your models here.

admin.site.register(Water_data)
```

- 結果，我們就可以管理 `water_signal_water_data`這一個table了，但我們其實是想要處理已經存在了data_table，要怎麼辦呢?
- 這個根據有經驗人士表示可以試試看`fake initial`，這個寫到這邊先停住，我們先完成其他功能
- TODO: fake initial

----

## Web API 回應JSON資料

### 關鍵字 `JsonResponse`

- 我們先自己製造資料，先不取資料庫的資料，簡化需求，只完成JSON的回應功能
- 先在 `water_signal/urls.py` 加入新path
```
path('data/last',  views.data_last),
```

- 並在 `water_signal/views.py` 加入新的function
```

...

from django.http import JsonResponse

...

def data_last(request):
    is_ng = False #True

    if is_ng:
        result = {'result':'NG', 'log':'no data in db'}
        return JsonResponse(result)
    else:
        data_dict = {
            "time": "2021-04-06 10:27:38",
            "water_level_1": 0,
            "water_level_2": 0
        }
        result = {'result':'OK', 'data':data_dict}
        return JsonResponse(result)
```

- 這樣就可以在網址 `http://localhost:8000/water_signal/data/last` 下取得json資料

----

## 接著我們要從資料庫中取資料，以web API回應JSON格式

[ref](https://blog.csdn.net/Gscsd_T/article/details/81913804)

- `Water_data.objects.all()` 我們可以取得所有資料 (對應的DB table為: `water_signal_water_data`
- 當我們要使用select來取部分資料時: `data = Water_data.objects.filter(data_time__gte=tm_start, data_time__lt=tm_end)`
  - __gte : 大於等於
  - __lte : 小於等於
  - __endswith : 以...結尾
- 要排序時，用 order_by :
  - ASC:  Water_data.objects.filter(data_time__gte=tm_start, data_time__lt=tm_end).order_by('data_time')
  - DESC: Water_data.objects.filter(data_time__gte=tm_start, data_time__lt=tm_end).order_by('-data_time')

- 所以我們可以用以下的function取得某時間區間的資料 (加在 water_signal/views.py 中)

```
def data_t1t2_4chart(request):
    if request.method == 'GET':
        tm_start = request.GET.get('tm_start')
        tm_end = request.GET.get('tm_end') # 用這個寫法! 和flask會比較類似
        if not tm_start:
            dt_now = datetime.datetime.now()
            tm_end = dt_now.strftime("%Y-%m-%d 00:00:00")
            tm_start = (dt_now - datetime.timedelta(days=7)).strftime("%Y-%m-%d 00:00:00")
        else:
            if not tm_end:
                tm_end = tm_start
                dt2 = datetime.datetime.strptime(tm_end,"%Y-%m-%d %H:%M:%S")
                tm_start = (dt2 - datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")

        print('data time: %s ~ %s' %(tm_start, tm_end))

        # get data from DB
        data = Water_data.objects.filter(data_time__gte=tm_start, data_time__lt=tm_end)

        dtime_list = []
        water_level_1_list = []
        water_level_2_list = []
        for item in data.values():
            dtime = item['data_time']
            str_dtime = dtime.strftime("%Y-%m-%d %H:%M:%S")
            water_level1 = item['water_level1']
            water_level2 = item['water_level2']
            dtime_list.append(str_dtime)
            water_level_1_list.append(water_level1)
            water_level_2_list.append(water_level2)
            print(str_dtime, water_level1, water_level2)

        data_dict = {'water_level_1':water_level_1_list, 'water_level_2':water_level_2_list
            , 'time':dtime_list}

        result = {'result':'OK', 'data':data_dict}
        return JsonResponse(result)

    elif request.method == 'POST':
        pass
```

- 當然，處理資料的function完成了，下一步就是要在`water_signal/urls.py`中登記，加入:
  - `path('data/t1t2/4chart',  views.data_t1t2_4chart),`

----

## 資料管理介面: 這是我超喜愛的Django功能

- 只需要在所需要的App下的 admin.py註冊就可以
- 以我的為例是: `water_signal/admin.py`，內容如下

```
from django.contrib import admin
from water_signal.models import Water_data

# Register your models here.

admin.site.register(Water_data)
```
- 產生的畫面如下:
![img](img/django_admin.png)

- Django預設會在資料表名稱後面加上s

### 進一步，更多的管理細部調整 (p8-19)

- 新增一個class來指定要顯示那些參數，我們修改`water_data/admin.py`如下:

```
from django.contrib import admin
from water_signal.models import Water_data

class Water_data_Admin(admin.ModelAdmin):
    list_display = ['data_time', 'water_level1', 'water_level2']

    class Meta:
        model =  Water_data

# Register your models here.

#admin.site.register(Water_data)
admin.site.register(Water_data, Water_data_Admin)
```

![img](img/django_admin2.png)

- 其他調整
  - 欄位可以直接編輯: `list_editable = ['water_level2']`
  - 可以搜尋: `search_fields = ['data_time']`



### 時間格式問題
[ref](https://blog.mounirmesselmeni.de/2014/11/06/date-format-in-django-admin/)

- 目前的時間格式看起來不太習慣，我都是習慣用 YYYY-MM-DD hh:mm:ss
- `water/settings.py` 加入設定如下:
- 這個設定是在設定en語系的，所以如果在 TIME_ZONE = 'Asia/Taipei' 時，就不會發生影響
- 另外，這邊的設定是影響全域的，就不需要每個models.py逐一去改
```
...

from django.conf.locale.en import formats as en_formats

...

#TIME_ZONE = 'Asia/Taipei'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

en_formats.DATETIME_FORMAT = 'Y-m-d H:i:s'
en_formats.DATE_FORMAT = 'Y-m-d'
en_formats.TIME_FORMAT = 'H:i:s'
```

----

### 前後端分離的作法 (我目前想到較方便的方式)

- 搞了一整天 static 都無法被存取到，又因為我根本就沒有再使用樣板，好像就不需要特別再搞樣板路徑....
- 目前，是將全部的html, css, js都放到static資料夾下，這樣再html檔中使用相對路徑就都沒有問題了
- 然後，再把原來的html中取用的 web api 因為移到django而路徑有變化的部分改正確
- 目前的想法是因為所有API我都已經在後端有設存取權限，所以這樣就算安全?!
- 全部放在 `water_signal\static\water_signal` 資料夾中
- 然後以 `http://127.0.0.1:8080/static/water_signal/watergate_overview.html` 去看網頁 (缺點是 static 會在 url 中)
- 結構會是這樣
```
./water_signal
  |
  |-- assets
  |-- css
  |-- img
  |-- js
  |-- vendor
  |-- index.html
  |-- watergate_overview.html
  ....
```

----

### 繼續實作login的功能 (和原來admin的登入頁分開)

說明一下這邊碰到的要點

- 確認是GET, POST: `request.method == 'POST'` 可以區分
- 取得form中的欄位
  - `username = request.POST.get('username')` --> 由測試結果來看，django中的parameter (如:url/api?para1=aaa&para2=bbb)好像就等於form的欄位，因為在GET, POST的這兩個取得方式都一樣 (記得flask這邊好像是分開的)

- 用`user = authenticate(username=username, password=password)` 來取得登入的user資訊，失敗的話，會取得None，所以用  `if not user` 就可以判斷是否ok
- 在用 `auth_login(request, user)` 進行登入的細項處理，如session要紀錄，並填入要送給前端的欄位之類的
- 做到這邊就可以 return 結果了
- 另外，因為django會對 POST 動作進行 csrf 的確認，所以需要對單一API先取消csrf的檢查，用 `@csrf_exempt` 裝飾子即可 (書上都是教用template的方式讓後端嵌入csrf資料，但這樣會前後端無法完全分離，不是我想要的!)

```
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            result = {'result':'NG', 'log':'username or password loss'}
            return JsonResponse(result)
        
        user = authenticate(username=username, password=password)
        if not user: #auth. fails
            result = {'result':'NG', 'log':'authentication fails'}
            return JsonResponse(result)
        
        auth_login(request, user)
        result = {'result':'OK'}
        return JsonResponse(result)
```

