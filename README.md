# finance_bot
_________________________
о программе
==============

телеграмм бот получает сообщение в виде `сумма%%комментарий`.
знак %% используется как разделитель
после получения сообщения бот заносит в базу данных : `сумма`, `комментарий`, `день`, `месяц`, `год`
как только данные внесены в базу данных бот отправляет `сохранено` в случае успеха и `ошибка` в случае если что то пошло не так
сумма может быть как положительной так и отрицательно, но обязательно целочисленного типа
комментарий не обязателен
_______________________________
настройка
========
в файле `main.py` установите свой `id` в переменную `selfid` и в переменную `token` свой токен полученный от `@BotFather`

_*бот хранит только ваши траты, это нужно чтобы никто другой не мог пользоваться этим ботом*_

для запуска программы откройте файл `open.file`

возможные ошибки
================
во избежание некоторых ошибок убедитесь что у вас установленны следующие модули
```Batchfile
pip install telebot
pip install sqlite3
pip install atetime
pip install pygame
pip install PIL 
```
_______________________
статистика
----------
откройте файл `stete.py` если все пройдет хорошо в директории где расположен файл появится изображение `tabl.py` там будут отображены ваша статистика за месяц

ежедневная статистика
---------------------
бот имеет единственную команду `/stat` которая выводит в чат сообщение о ваших тратах в течение дня
