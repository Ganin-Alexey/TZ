# ТЗ
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Задача: спроектировать и разработать API для системы опросов пользователей.
Функционал для администратора системы:
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Выполненное ТЗ
--------------
Инструкция по разворачиванию приложения:
------------------------------------------
1). Клонируем этот репозиторий в любой IDE.

2). Устанавливаем все зависимости, которые перечислены в "requirements.txt". Можно командой  "pip install -r requirement.txt".

3). Запускаем проект (обязательно на 8000 порте) командой "python manage.py runserver 8000".

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Инструкция по работе с API: 
---------------------------
Доступные Endpoint'ы можно посмотреть по адресу "http://127.0.0.1:8000/".

1). Для получения доступа к админке переходим по адресу "http://127.0.0.1:8000/admin/", Email: "123@mail.ru", Пароль: "123":
  - Можно настроить опросы, вопросы к ним.
  - Посмотреть имеющиеся вопросы и ответы к ним.

2). Получение списка активных опросов - Нужно перейти по адресу "http://127.0.0.1:8000/interrogations/" или воспользоваться API-endpoint'ом,
для этого нужно перейти по адресу "http://127.0.0.1:8000/api-interrogations/".

3). Прохождение опроса - Можно перейти по адресу "http://127.0.0.1:8000/interrogations/" и нажать на один из перечисленных опросов,
а можно перейти по ссылке "http://127.0.0.1:8000/interrogations/detail/<Тут нужно указать ID вопроса>/". Или же "http://127.0.0.1:8000/api-interrogations/detail/<Тут нужно указать ID вопроса>/" для получения ответа в формате json.

4). Получение пройденных пользователем опросов - Можно ерейти по адресу "http://127.0.0.1:8000/interrogations/" и нажать "Смотреть пройденные",
а можно перейти по ссылке "http://127.0.0.1:8000/interrogations/answered/<Тут нужно указать ID пользователя>/". Или же воспользоваться адресом "http://127.0.0.1:8000/api-interrogations/answered/<Тут нужно указать ID пользователя>/" для получения ответа в формате json. 
