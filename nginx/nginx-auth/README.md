# nginx-auth

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html)
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip). Установите авторизованный вход для учетки: `design:SteveJobs1955`, т.е. логин `design`, пароль `SteveJobs1955`.
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip). Установите авторизованный вход для учетки: `marketing:marketingP@ssword`.
6. Учетка `design` не должна иметь доступ на другие пути, тоже самое касается других учеток.

---

### Ответ

```
server {
    listen 8080;
    server_name example.com;

    location / {
        root /var/www/html;
        index index.html;
        try_files $uri $uri/ =404;
    }

    location /images {
        auth_basic "Private Images";
        auth_basic_user_file /var/www/cats_passwd;

        alias /var/www/cats;
    }

    location /gifs {
        auth_basic "Private Gifs";
        auth_basic_user_file /var/www/gifs_passwd;

        alias /var/www/gifs;
    }
}
```