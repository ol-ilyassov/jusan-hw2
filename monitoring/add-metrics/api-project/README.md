# FastAPI-Final

Домашняя работа #4 в рамках курса **Jusan Singularity** направления **DevOps**. 

Выполнил: **Olzhas Ilyassov**.

Задачи направленные на разработку простого сервисного приложения с заданными API методами. 

## Описание

В рамках домашнего задания реализованы следующие методы:
```
- GET: /sum1n/{n}
- GET: /fibo?n={n}
- POST: /reverse
- GET: /list
- PUT: /list
- POST: /calculator
```

Подробнее c API методами можно ознакомиться в Swagger документации локально развернутого приложения по пути: [/docs](http://127.0.0.1:8000/docs).

## Применение

### Зависимости

- Операционная система Ubuntu 22.04 LTS+.
- Компилятор языка Python3.6+. 
- Пакеты "fastapi" и "uvicorn".

Подробнее с техническими зависимостями проекта можно ознакомиться в файле [requirements.txt](./requirements.txt).

### Установка

- Базовая установка:
```bash
# обновление пакетов ОС.
sudo apt update

sudo apt upgrade

# установка компилятора Python.
sudo apt install python3

python3 --version

# установка пакет менеджера Python.
sudo apt install python3-pip

# установка Python утилиты.
sudo apt install uvicorn

# дополнительно: утилита make.
sudo apt-get install build-essential
```

- Установка локального окружения:
```bash
python3 -m venv .venv

source .venv/bin/activate
```

- Установка зависимостей
```bash
# главные пакеты зависимости:
pip install "fastapi[standard]" 

pip install "uvicorn[standard]"

# установка всех зависимостей проекта:
pip install -r requirements.txt
```

### Запуск

Запуск проекта должен происходить в корневой папке проекта. Существует несколько вариантов запуска серверного приложения:

1) Запуск приложения (через uvicorn утилиту):
```bash
uvicorn main:app
```

2) Запуск приложения в режиме разработки (через fastapi утилиту):
```bash
fastapi dev main.py
```

3) Упрощенный вариант с помощью готовой команды make (требуется установленный пакет make):
```bash
make run
```

## Лицензия

Этот проект лицензирован по лицензии MIT — подробности см. в файле [LICENSE.md](./LICENSE.md).