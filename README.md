# Домашнее задание к лекции «Flask»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория. 

## Задание 1

Вам нужно написать REST API (backend) для сайта объявлений.
Удалять/редактировать может только владелец объявления.
В таблице с пользователями должны быть как минимум следующие поля: идентификатор, почта и хэш пароля.

## Как сдавать задачи

1. Инициализируйте на своём компьютере пустой Git-репозиторий
2. Добавьте в этот же каталог необходимые файлы
3. Сделайте необходимые коммиты
4. Создайте публичный репозиторий на GitHub и свяжите свой локальный репозиторий с удалённым
5. Сделайте пуш (удостоверьтесь, что ваш код появился на GitHub)
6. Ссылку на ваш проект отправьте в личном кабинете на сайте [netology.ru](http://netology.ru/)
7. Задачи, отмеченные как необязательные, можно не сдавать, это не повлияет на получение зачета (в этом ДЗ все задачи являются обязательными)
8. Любые вопросы по решению задач задавайте в чате Slack, но мы не сможем проверить или помочь, если вы пришлете:
* архивы;
* скриншоты кода;
* теоретический рассказ о возникших проблемах.

# Команды для запуска приложения:
## docker build --tag flask_hw .
## docker run --name flask_homework -d -p 5000:5000 flask_hw