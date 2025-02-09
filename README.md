# Система управления заказами в кафе

## Описание
Это веб-приложение на Django, предназначенное для управления заказами в кафе. Приложение позволяет добавлять, удалять, искать, изменять и отображать заказы. Каждый заказ содержит уникальный идентификатор, номер стола, список заказанных блюд с ценами, общую стоимость и статус.

## Стек технологий
- Python 3.12+
- Django 5+
- PostgreSQL (для хранения данных)
- HTML/CSS (для интерфейса)
- DjangoRestFramework 3+ (API)
- drf-yasg 1.20+ (для Swagger документации)

## Функционал
P.S. Некоторые вещи довольно сырые, поэтому если что-то ругается просто перезагрузи страницу, хоть такого, вроде, и не должно быть)

### Стартовая страница
- **URL**: `/`
- Форма для поиска заказов по номеру стола и статусу.
- Обработка GET запроса вида `/search/?table_number=0&status=A`, где:
  - `table_number` — номер стола.
  - `status` — статус заказа: 
    - `A` — все статусы.
    - `W` — в ожидании.
    - `R` — готово.
    - `P` — оплачено.

### Страница с заказами в ожидании
- **URL**: `/waiting/`
- Отображает все заказы со статусом "В ожидании".

### Страница с готовыми заказами
- **URL**: `/ready/`
- Отображает все заказы со статусом "Готово".

### Страница с оплачеными заказами
- **URL**: `/paid/`
- Отображает все заказы со статусом "Оплачено".
- Возможность просмотра общей выручки по каждому столу, а также суммарной выручки.

### Управление заказами
- На страницах **Стартовая**, **Ожидание**, **Готово**, **Оплачено** можно перейти на подробное описание заказа.
- В интерфейсе можно:
  - Изменять содержимое заказа.
  - Изменять статус заказа.
  - Удалить заказ.

## Начало работы

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/khrushchew/TestCafeteria.git
   ```

2. Установите и активируйте виртуальное окружение (Далее в Readme примеры для Unix):
   - **Для Unix**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Для Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Убедитесь, что всё работает:
   ```bash
   pip list
   ```
   Должен быть только `pip` в списке установленных пакетов.

4. Установите необходимые зависимости из файла `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. Создайте базу данных через PgAdmin или psql и укажите её данные в файле `Cafeteria/settings.py`:
   Измените настройки подключения к базе данных:
   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "cafeteria",
           "USER": "postgres",
           "PASSWORD": "12345678",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }
   ```

6. Если миграции ещё не созданы, перейдите в директорию, где находится файл `manage.py`, и выполните команду для создания миграций:
   ```bash
   python3 manage.py makemigrations Core
   ```

7. Примените миграции:
   ```bash
   python3 manage.py migrate
   ```

8. Теперь, когда всё настроено, запустите сервер командой:
   ```bash
   python3 manage.py runserver [Порт]
   ```
   Замените `[Порт]` на нужный вам порт, если хотите использовать нестандартный.

Теперь приложение готово к использованию!

## Админка

Для доступа к админке нужно создать суперпользователя. Введите в терминале команду:
```bash
python3 manage.py createsuperuser
```

Следуйте инструкциям в терминале для ввода логина, пароля и почты.

После этого перейдите по адресу `/admin/` в браузере.

Введите логин и пароль, чтобы войти в админку и насладитесь её сыростью :) 
Тут можно добавь всё необходимое без использования API

**P.S.** Поле `total_price` в модели не пересчитывается через админку. Это можно исправить, но мне было лень :<

## Документация

Дёрни за ручку /api/swagger/ - увидишь цветную красоту, которая пока особо не имеет смысла, кроме get запросов или delete, но она есть, а значит это круто

## API

## API

Есть несколько роутов:

- **/api/dishes/** — взаимодействие с блюдами
- **/api/tables/** — взаимодействие со столами
- **/api/orders/** — взаимодействие с заказами

Протестировать всё можно через Postman, так как Swagger сыроват. К тому же у заказов нет `update`, `partial_update` и `destroy` в контроллерах. Почему? Смотри P.S. в админке, там железный аргумент.

Вот пример данных для разных роутов:

### Для `orders`:
```json
{
    "table_number": 4,
    "items": [2, 3],
    "status": "W"
}
```

### Для `tables`:
```json
{
    "position": 1
}
```

### Для `dishes`:
```json
{
    "name": "Ля ля ля",
    "price": 10000
}
```

Столы и блюда поддерживают все возможные CRUD операции.

Если будут вопросы, можно задать их по почте или в Telegram.
