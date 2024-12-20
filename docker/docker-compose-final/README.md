# docker-compose-final

В данном задании научимся делать связку контейнеров с помощью `docker-compose`.

### Задание

1. Вся работа должна выполняться в репозитории текущего модуля в папке `docker-compose-final`.
2. Скачать конфигурационный файл [jusan-docker-mount.conf][jusan-docker-mount.conf] с помощью `curl`.
3. Скачать конфигурационный файл [jusan-docker-mount.zip][jusan-docker-mount.zip] с помощью `curl`.
   Разархивировать архив с помощью `unzip`.
4. Написать `docker-compose.yml`, который:

   - имеет два сервиса `nginx` и `api`;
   - сервис `api` использует образ `jusan-fastapi-final:dockerized`;
   - сервис `api` имеет имя контейнера `jusan-compose-final`;
   - сервис `nginx` использует образ `nginx:mainline`.
   - сервис `nginx` перенаправляет запрос с хостового порта 8787 на 80 порт контейнера;
   - сервис `nginx` монтирует скачанный `jusan-docker-mount.conf` внутрь контейнера.
   - сервис `nginx` монтирует распакованный `jusan-docker-mount.zip` внутрь контейнера. Определите куда нужно монтировать по конфигурационному файлу;
   - сервис `nginx` монтирует `jusan-fastapi-final.conf` внутрь контейнера. Этот файл будет создан в следующем шаге.
   - сервис `nginx` зависит от `api`;
   - сервис `nginx` имеет имя контейнера `jusan-nginx-final`;
   - оба сервиса перезапускаются в случае провала;

5. Создать конфигурационный файл `jusan-fastapi-final.conf` для nginx, который:

   - слушает 80 порт;
   - имеет имя `jusan.docker-compose`;
   - перенаправляет запросы на контейнер `jusan-compose-final`;

6. Запустить `docker-compose` на фоне.
7. Посмотрите на состояние контейнеров:

```bash
docker-compose ps
```

6. Посмотрите на логи контейнеров:

```bash
docker-compose logs nginx
docker-compose logs api
```

7. Запушить в гит:

   - `docker-compose.yml`,
   - `jusan-fastapi-final.conf`,
   - распакованный `jusan-docker-mount`,
   - скачанный `jusan-docker-mount.conf`.

8. Прислать ссылку на репозиторий.

[jusan-docker-mount.conf]: https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
[jusan-docker-mount.zip]: https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip

---

### Ответ

```bash
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf

curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
unzip jusan-docker-mount.zip

nano docker-compose.yml
```

```docker
services:
  api:
    image: jusan-fastapi-final:dockerized
    container_name: jusan-compose-final
    restart: on-failure

  nginx:
    image: nginx:mainline
    container_name: jusan-nginx-final
    ports:
      - "8787:80"
    volumes:
      - ./jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf
      - ./jusan-docker-mount:/var/www/example
      - ./jusan-fastapi-final.conf:/etc/nginx/conf.d/jusan-fastapi-final.conf
    depends_on:
      - api
    restart: on-failure
```

```bash
nano jusan-fastapi-final.conf
```

```docker
server {
    listen 80;
    server_name jusan.docker-compose;

    location / {
        proxy_pass http://api:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash

docker compose up -d

docker exec -it jusan-nginx-final /bin/bash
cd /etc/nginx/conf.d
rm default.conf
nginx -s reload
exit

curl -H "Host: example.com" http://127.0.0.1:8787

curl -H "Host: jusan.docker-compose" http://127.0.0.1:8787/sum1n/3

docker compose ps

docker compose logs nginx
docker compose logs api
```