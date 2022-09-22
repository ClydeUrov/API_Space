# Космический Телеграм

Скачивает картинки с сайтов NASA и SpaceX. 
Выгружает скачанные картинки в телеграмм канал.

### Как установить 

Для скачивания картинок с сайта NASA необходим NASA_TOKEN. 
Получить его можно на сайте [{ NASA APIs }](https://api.nasa.gov/). 
Пример:
```
NASA_TOKEN='mlafKIH1LG1N5BxRlz4lY1OWaEelQVgIvpVkygBB'
```
Вносим его в файл `.env` для запуска программ **fetch_nasas_images.py** и **fetch_nasas_epic.py**.
___
Для загрузки картинок на телеграмм канал необходим TG_TOKEN и TG_CHAT_ID.
Получаем TG_TOKEN в телеграмме у *@BotFather*.
Пример:
```
TG_TOKEN='5770283337:AAEa868qn7PkD-vx4Dp75mmzPGxvtovcR1g'
```
Получаем TG_CHAT_ID телеграмм бота в телеграмме у *@getmyid_bot* или указываем ссылку на свой телеграмм канал.
Пример: 
```
TG_CHAT_ID="@devman_space_images"
```
Вносим их в файл `.env` для запуска программы **telegram_bot.py**.

___
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
___
### Запуск программ
##### Выгрузить картинки в телеграмм бота
Принимает на вход командной строки промежуток времени (секунды), через который будет выгружаться одна картинка с папки ``\image`` в группу или канал, ID которого указан в папке `.env`.
Eсли программе не задавать начальный параметр, то картинки будут выгружаться каждые 4 часа (14400 секунд)
Пример ввода: 
*Загружает картинку раз в 14400 секунд:*
```
..\API_Space>python3 telegram_bot.py
```
*Загружает картинку раз в 10 секунд:*
```
..\API_Space>python3 telegram_bot.py -d 10
```

Так же программа перехватывает ошибку `telegram.error.NetworkError` при сбоях в интернет-соединении и запускает код снова.
___
Для остановки работы кода ввести:
``Ctrl+C`` вызвав ошибку `KeyboardInterrupt`
___
##### Скачать картинки NASA EPIC
Загружает в папку ``\image`` картинки [NASA EPIC](https://api.nasa.gov/) с сайта. Количество загружаемых картинок умолчанию — 5.
Пример ввода:
*Скачать 5 картинок:*
```
..\API_Space>python3 fetch_nasas_epic.py
```
*Скачать 10 картинок:*
```
..\API_Space>python3 fetch_nasas_epic.py -d 10 
```
___
##### Скачать картинки NASA APOD
Загружает в папку ``\image`` картинки [NASA APOD](https://api.nasa.gov/) с сайта.
На данный сайт каждый день загружается по одной картинке от NASA. 
По умолчанию скачивает картинки начиная с `2022-08-28` по сегодняшнюю дату. 
Пример ввода:
*Загрузить картинки с 22-08-28:*
```
..\API_Space>python3 fetch_nasas_images.py
```
Для указания другой даты скачивания вводим в формате [year]-[month]-[day].
*Загрузить картинки с 22-08-05:*
```
..\API_Space>python3 fetch_spacex_images.py -d 22-08-05
```
___
##### Скачать картинки SpaceX
Загружает в папку ``\image`` картинки с последнего запуска с сайта [API SpaceX]('https://api.spacexdata.com/v5/launches/latest'). В случае, если нету картинок в последнем запуске — выдаёт ошибку *EmptyListError*.
Пример ввода:
*Выгрузить картинки последнего запуска:*
```
..\API_Space>python3 fetch_spacex_images.py
```
Каждый запуск имеет свой ID. Для указания ID определённого запуска вводим как указано на примере.
*Выгрузить картинки запуска с ID 5eb87d47ffd86e000604b38a:*
```
..\API_Space>python3 fetch_spacex_images.py -d 5eb87d47ffd86e000604b38a
```
Список нескольких вариантов запусков, в которых имеются картинки:
```
5a9fc479ab70786ba5a1eaaa
5eb87d47ffd86e000604b38a
5e9e3032383ecb267a34e7c7
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).