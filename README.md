Задание:
-------

* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель `Item` с полями `(name, description, price) `
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении
      этого метода c бэкенда с помощью python библиотеки stripe должен выполняться
      запрос` stripe.checkout.Session.create(...)` и полученный session.id выдаваться в результате запроса
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о
      выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на `/buy/{id}`, получение
      session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout
      форму `stripe.redirectToCheckout(sessionId=session_id)`

* Залить решение на Github, описать запуск в README.md

* Запуск используя `Docker`

* Просмотр Django Моделей в Django Admin панели - доступно по адресу `127.0.0.1:8000/admin`



## Для запуска заполните в settings поля STRIPE_PUBLISHABLE_KEY и STRIPE_SECRET_KEY

Publishable key:
https://dashboard.stripe.com/apikeys

Secret key:
https://dashboard.stripe.com/apikeys


Запуск
------

```
git clone https://github.com/BenitoSwaggolini/Stripe-task.git
cd stripe_task
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Для админки:
```
python manage.py createsuperuser
```

Запуск Docker
------

```
git clone https://github.com/BenitoSwaggolini/Stripe-task.git
docker-compose up -d
```



Главная страница: http://127.0.0.1:8000

Если сервер не отдаёт информацию, подождите пару секунд и перезагрузите страницу

Сервис
------


* `admin/` - Админка
* `buy/<item_id>` - Покупка товара по id
* `item/<item_id>` - Отдаёт информацию об id сессии

