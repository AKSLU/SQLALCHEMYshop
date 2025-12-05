# SQLALCHEMYshop

Пример использования SQLAlchemy для работы с магазином, продуктами и пользователями на SQLite.

---

## Требования

* Python 3.10+
* `SQLAlchemy`

Установите через pip:

```bash
pip install sqlalchemy
```

---

## Использование

1. Клонируйте репозиторий:

```bash
git clone https://github.com/AKSLU/SQLALCHEMYshop.git
cd SQLALCHEMYshop
```

2. Запустите скрипт:

```bash
python app.py
```

3. Скрипт создаёт базу `example.db`, добавляет продукты, магазин и пользователей, демонстрирует добавление и удаление пользователей, вывод всех записей.

Пример вывода:

```
Добавлен: User(id=1, username='akslu1', email='akslu@1')
Добавлен: User(id=2, username='akslu2', email='akslu@2')
delate: User(id=1, username='akslu1', email='akslu@1')

All products:
Product(id=1, price=200, category='Food', article='A1')
Product(id=2, price=60, category='Cundy', article='A2')

All shops:
Store(id=1, name='Shop1', ur_address='adress1')

All users:
User(id=2, username='akslu2', email='akslu@2')
```

---

## Структура проекта

* `Product` — продукты магазина.
* `Store` — магазины.
* `User` — пользователи.
* Методы `add_user` и `delete_user` демонстрируют добавление и удаление пользователей.
* SQLAlchemy ORM используется для управления базой данных.
