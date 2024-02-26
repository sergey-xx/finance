## Тестовый проект по работе с Django и Stripe API


### Каталог
http://mazilin.ddns.net/items/

### Заказ
http://mazilin.ddns.net/items/order/

Добавлена возможность добавлять купоны через Админку

Установка в докере:

- cкопировать docker-compose-production в папку на сервере
- cкопировать папку со статикой django
- cоздать .env файл с переменными
```
SECRET_KEY=<секретный ключ Джанго>
STRIPE_SECRET_KEY_TEST=<STRIPEAPIKEY>
SERVER_IP=<IP вашего сервера>
DOMAIN_NAME=<Доменное имя сервера>
```

В папке выполнить
```
sudo docker compose -f docker-compose.production.yml up -d 
```

Скопировать статику
```
sudo docker compose -f docker-compose.production.yml cp collected_static/. gateway:static/
```

Создать суперпользователя
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
```
