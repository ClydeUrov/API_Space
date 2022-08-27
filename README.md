# Космический Телеграм.

Принимает на вход командной строки промежурок времени (секунды), через который будет выгружаться одна картинка в группу [Space Images](https://t.me/devman_space_images).
Eсли программе не задавать начальный параметр, то картинки будут выгружаться каждые 4 часа (14400 секунд)
Пример ввода: 
```
..\API_Space>python3 telegram_bot.py -d 10
```
``Загружает картинку раз в 10 секунд.``
```
..\API_Space>python3 telegram_bot.py
```
``Загружает картинку раз в 14400 секунд.``

Для остановки работы кода ввести:
``Ctrl+C``

Программа скачивает картинки NASA и SpaceX.
Пример ввода:
```
..\API_Space>python3 fetch_nasas_epic.py
```
Загружает в папку ``\image`` картинки [NASA EPIC](https://api.nasa.gov/) с сайта.
```
..\API_Space>python3 fetch_nasas_images.py
```
Загружает в папку ``\image`` картинки [NASA APOD](https://api.nasa.gov/) с сайта.
```
..\API_Space>python3 fetch_spacex_images.py
```
Загружает в папку ``\image`` картинки с сайта [API SpaceX]('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a').

### Как установить 

Для скачивания картинок с сайта NASA необходим NASA_TOKEN. 
Получаем его на сайте [{ NASA APIs }](https://api.nasa.gov/). 
Пример:
```
NASA_TOKEN = 'mlafKIH1LG1N5BxRlz4lY1OWaEelQVgIvpVkygBB'
```

Для загрузки картинок на телеграмм канал необходим TG_TOKEN.
Получаем его в телеграмме у @BotFather.
Пример токена из телеграмм:
```
TG_TOKEN = '5770283337:AAEa868qn7PkD-vx4Dp75mmzPGxvtovcR1g'
```
Вносим NASA_TOKEN и TG_TOKEN в файл `.env`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).