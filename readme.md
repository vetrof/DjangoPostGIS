Описание проекта для GitHub

# Places Management with PostGIS

Это Django-приложение для управления географическими данными с использованием PostGIS. В проекте реализована возможность хранения местоположений (координат) и работы с ними через админку и API.

## Используемые технологии

- **Django**: Веб-фреймворк для разработки серверной части.
- **PostGIS**: Расширение PostgreSQL для работы с географическими данными.
- **Leaflet**: Библиотека для отображения карт в админке.
- **GDAL**: Инструмент для обработки географических данных.

## Основные функции

- Хранение информации о местах с использованием поля `PointField`.
- Управление географическими данными через админку Django с интерактивной картой (Leaflet).
- Пространственные запросы к базе данных (например, поиск мест в заданном радиусе).
- Поддержка кастомных настроек отображения карты.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-аккаунт/places-postgis.git
   cd places-postgis

	2.	Убедитесь, что установлены зависимости для работы с PostGIS и GDAL:
	•	Для Ubuntu/Debian:

sudo apt-get update
sudo apt-get install -y gdal-bin libgdal-dev proj-bin libproj-dev


	•	Для MacOS:

brew install gdal proj


	3.	Установите зависимости Python:

pip install -r requirements.txt


	4.	Настройте базу данных PostgreSQL с PostGIS:

CREATE DATABASE places_db;
CREATE EXTENSION postgis;


	5.	Примените миграции:

python manage.py migrate


	6.	Создайте суперпользователя:

python manage.py createsuperuser


	7.	Запустите сервер разработки:

python manage.py runserver



Настройка Leaflet

По умолчанию карта в админке использует OpenStreetMap с заданным центром и уровнем зума. Вы можете изменить настройки в settings.py:

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (50.4501, 30.5234),  # Центр карты (широта, долгота)
    'DEFAULT_ZOOM': 12,                   # Уровень зума
}

Использование
	1.	Перейдите в админку по адресу /admin/places/place/.
	2.	Добавляйте и редактируйте места, задавая их координаты на карте.
	3.	Выполняйте пространственные запросы через ORM Django.

Пример пространственного запроса

Пример кода для поиска всех объектов в радиусе 10 км от заданной точки:

from django.contrib.gis.measure import D  # Для измерения расстояний
from django.contrib.gis.geos import Point
from places.models import Place

point = Point(30.5238, 50.4501)  # Долгота и широта
places = Place.objects.filter(location__distance_lte=(point, D(km=10)))

Зависимости
	•	Python 3.10+
	•	Django 5.1+
	•	PostgreSQL с PostGIS
	•	GDAL и Proj

Лицензия

Этот проект распространяется под MIT License.

.env sample

POSTGRES_DB=postgres_database
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=12345
POSTGRES_HOST=db
POSTGRES_PORT=5432

для пересборки го приложения  
docker compose restart go
