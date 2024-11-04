# dockerize

В данном задании докеризируем свой проект из задания `jusan-fastapi-final`.

### Полезное

- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [Docker Push for Publishing Images](https://www.section.io/engineering-education/docker-push-for-publishing-images-to-docker-hub/)

### Задание

1. Склонируйте содержимое репозитория `jusan-fastapi-final` в репо `jusan-docker/dockerize`.
   Работу будем ввести в нем.
2. Напишите для этого проекта Dockerfile, который запускает API на порту 8080.
3. Произвести сборку образа с именем `jusan-fastapi-final` и тегом `dockerized`.
4. Проверьте на наличие своего образа в вашей системе, перечислите все образы.
5. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 8080 на 8080 порт контейнера;
   - имя контейнера `jusan-dockerize`;
   - использует наш собранный образ.

6. Выполненные команды из шагов 3 и 5 записать в файл `dockerize/solution.sh`.
7. Запушить в репозиторий `jusan-docker`. В папке `dockerize` должны быть:
   - получившийся `Dockerfile`.
   - `solution.sh`
   - содержимое репозитория `jusan-fastapi-final`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-dockerize.sh

---

### Ответ

```bash
# условное клонирование:
cp -r ../../python/api/fastapi-final/api-project .

cd docker/dockerize

touch Dockerfile
```

```dockerfile
FROM python:latest

WORKDIR /app

COPY ./api-project/requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./api-project/main.py main.py

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

```bash
docker build -t jusan-fastapi-final:dockerized .

docker images

docker run -d \
   -p 8080:8080 \
   --name jusan-dockerize \
   jusan-fastapi-final:dockerized
```