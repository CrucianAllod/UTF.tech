# FoodTest Project

Это проект REST API для ресторана, реализованный с использованием Django и Django REST Framework. Проект содержит модели категорий блюд и самих блюд, а API возвращает данные в следующем формате:
```json
[
    {
        "id": 233,
        "name_ru": "Напитки",
        "name_en": "Drinks",
        "name_ch": null,
        "order_id": 2,
        "foods": [
            {
                "internal_code": 2002,
                "code": 1002,
                "name_ru": "Смузи из манго",
                "description_ru": "Свежий манго с йогуртом",
                "description_en": null,
                "description_ch": null,
                "is_vegan": true,
                "is_special": false,
                "cost": "450.00",
                "additional": []
            }
        ]
    },
    {
        "id": 232,
        "name_ru": "Основные блюда",
        "name_en": "Main courses",
        "name_ch": null,
        "order_id": 1,
        "foods": [
            {
                "internal_code": 2001,
                "code": 1001,
                "name_ru": "Стейк из лосося",
                "description_ru": "Свежий норвежский лосось с овощами",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "1200.00",
                "additional": []
            }
        ]
    }
]
```

# Стек технологий

- Django 5.0.7
- Django REST Framework
- PostgreSQL
- Docker

# Структура проекта
```markdown
.
├── .gitignore
├── food/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── foodtest/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```
# Предварительные настройки

В файле foodtest/settings.py настроены:

- Подключение к PostgreSQL через переменные окружения:
  - POSTGRES_DB (по умолчанию: fooddb)
  - POSTGRES_USER (по умолчанию: fooduser)
  - POSTGRES_PASSWORD (по умолчанию: foodpass)
  - POSTGRES_HOST (по умолчанию: db)
  - POSTGRES_PORT (по умолчанию: 5432)

- Статика:
    - STATIC_URL задан как /static/
    - STATIC_ROOT – каталог, куда собираются статические файлы: BASE_DIR/staticfiles

# Запуск проекта через Docker Compose

Проект включает файлы:

- Dockerfile – для сборки образа приложения.
- docker-compose.yml – для объединения контейнеров приложения и базы данных.

# Шаги запуска:

1. Клонируйте репозиторий:
```bash
  git clone https://github.com/CrucianAllod/UTF.tech.git
  cd UTF.tech
```

2. Соберите и запустите контейнеры:

```bash
  docker-compose up --build
```
- Контейнер db запустит PostgreSQL.
- Контейнер app выполнит миграции, заполнит базу тестовыми данными и запустит приложение.

3. Доступ к API: API будет доступно по адресу: http://localhost:8000/api/v1/foods/.

# Использование API
Пример запроса:
- Получение списка категорий с блюдами:
```bash
  GET http://localhost:8000/api/v1/foods/
```
Ответ будет иметь формат, приведённый выше.