# 27.2. Docker Compose

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.
В рамках учебного курсового проекта реализована бэкенд-часть SPA веб-приложения.

При регистрации пользователь, помимо обязательных полей __"email"__ и __"password"__ может также передать поле __"tgm_id"__ с своим идентификатором в Telegram. В этом случае привычки, в которых указано время выполнения (параметр __"when"__) при наступление этого времени будут присылаться ботом в мессенджере Telegram.

Далее указанные параметры "email" и "password" используются для получения токена доступа.

Токен передается в заголовках запросов с именем 'Authorization': 'Bearer {access_token}' и необходим для доступа ко всем запросам работы с данными "Habit (Привычка)".

Необходимые поля для запросов можно посмотреть в докумментации по ссылкам ниже.

## Запуск сервиса
1. Установите Docker
2. Перейдите в корневую папку проекта (где располагается файл __docker-compose.yaml__)
3. Cоздайте файл ___.env___ (или переименуйте __.env-sample__) и установите необходимые значения переменных (пароль базы данных, токен и chat_id для Telegram).
4. Запустите терминал в корневой папке и выполните команды
   - __docker-compose build__
   - __docker-compose up -d__
   - __docker-compose exec app python3 manage.py loaddata data.json__ (создает пользователей и несколько привычек)
5. Контейнер создан и запущен.


* Пользователи и пароли по умолчанию (для проверяющего):
    - ID=1 admin@example.com - 123456
    - ID=2 user@example.com - user1user
    - ID=3 guest@example.com - guest1guest
* Для пользователя __user@example.com__ с ID=2 будет установлен __"tgm_id"__ указанный в .env файле под параметром __TELEGRAM_CHAT_ID__.  

### Основные URL
- [POST] http://127.0.0.1:8000/users/register/ - регистрация пользователя
- [POST] http://127.0.0.1:8000/users/token/ - получение JWT токена
- [GET] http://127.0.0.1:8000/habits/ - получение списка своих привычек /для авторизованных пользователей/
- [GET] http://127.0.0.1:8000/habits/{id}/ - получение информации о конкретной привычке /для авторизованных пользователей/
- [GET] http://127.0.0.1:8000/habits/public/ - получение списка всех публичных привычек /для авторизованных пользователей/
- [POST] http://127.0.0.1:8000/habits/create/ - добавление привычки /для авторизованных пользователей/
- [PATCH] http://127.0.0.1:8000/habits/{id}/update/ - peдактирование привычки /для авторизованных пользователей/
- [DELETE] http://127.0.0.1:8000/habits/{id}/delete/ - удаление привычки /для авторизованных пользователей/
- http://127.0.0.1:8000/docs/, http://127.0.0.1:8000/swagger/, http://127.0.0.1:8000/redoc/ - документация для API
