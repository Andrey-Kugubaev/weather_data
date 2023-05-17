# Тестовое задание на позицию python-разработчик в компанию DataFort
![Python](https://img.shields.io/badge/Python-3.10.4-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.36-green)
![Pydantic](https://img.shields.io/badge/Pydantic-1.10.7-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.6-green)
![Schedule](https://img.shields.io/badge/Schedule-1.2.0-green)
![Docker](https://img.shields.io/badge/Docker-grey)
![Flake8](https://img.shields.io/badge/flake8-grey)
<br>
## Оглавление:

- [Введение](#введение)
- [Список городов](#cписок-городов)
- [Погодные характеристики](#погодные-характеристики)
- [Инфраструктура](#инфраструктура)
- [Мониторинг](#мониторинг)
- [Инструкция по запуску](#инструкция-по-запуску)
----
### <anchor>Введение</anchor>
_Сервис по сбору информации о показателях климатических условий заданных мест для дальнейшего использования в задачах компании._

_Информация собирается с сайта https://openweathermap.org/ для 50 самых больших городов мира.
Запись в базу данных ведется каждый час._

----
### <anchor>Список городов</anchor>
Список городов собирается с заданного файла с данными.
Для каждого города сохраняется:
- Название;
- Координата северной широты;
- Координата восточной долготы;
- Численность населения.
----
### <anchor>Погодные характеристики</anchor>
Сайт https://openweathermap.org/ позволяет получить большое количетсво параметров климатических условий.
В настоящем проекте для каждого города, по заданным координатам, сохряняются следующие данные (_текущие значения на время сохранения_):
- Температура воздуха;
- Темперутара воздуха "по ощущениям";
- Влажность воздуха.

Все данные передаются серверу в метрической системе. 

----
### <anchor>Инфраструктура</anchor>
- Библиотека **Pydantic**
  - Библиотека для валидации данных, полученных из файла (для списка городов) или по api (для погодных данных)
- **SQLAlchemy**
  - Для работы с базой данных использована SQLAlchemy
- База данных **PostgeSQL**
  - Данная база данных выбрана как одна из самых удобных и популярных баз реляционного типа;
  - В проекте использованы две таблицы. Основая с информацие о погоде и дополнительная с информацией о городах. Данная структура является самой удобной, отвечающей поставленной задаче;
- Язык програмирования и версия **Python 3.10**
  - Данная версия языка поддерживает все необходимые версии библиотек;
- Библиотека **schedule**
  - Для периодического обращения сервиса для получения данных о погоде использованная библиотека schedule, позволяющая настроить расписание работы необхолимых функций;
----
### <anchor>Мониторинг</anchor>
- В приложении добавлена возможность онлайн мониторинга запросов к базе данных с помощью сервиса
[Sentry](https://sentry.io).
- Интструкция по пользованию серисом [тут](https://docs.sentry.io/platforms/python/?original_referrer=https%3A%2F%2Fwww.google.com%2F)
----
### <anchor>Инструкция по запуску</anchor>

1. Создаем .env и заполняем переменные окружения:<br>
`API_KEY = ваш api-ключ от сайта https://openweathermap.org/` <br>
`DATABASE_URL = postgresql://postgres:postgres@db:5432/postgres`<br>
`SENTRY_DSN = ваш dsn-ключ проекта на sentry.io`<br>
`DB_ENGINE = postgres`<br>
`DB_NAME = postgres`<br>
`POSTGRES_USER = postgres`<br>
`POSTGRES_PASSWORD = postgres`<br>
`DB_HOST = db`<br>
`DB_PORT = 5432`<br>

2. Устанавливаем `Docker`

3. Собираем `docker-compose`<br>
`docker-compose up -d --build`

4. Останавливаем и удаляем контейнеры:<br>
`docker-compose down -v`
----
