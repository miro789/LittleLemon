# Django Backend Framework Project

## Overview
This project is designed to provide a hands-on experience in creating a Backend Framework and APIs using Django. It helps in understanding the working of the Django Framework, creating APIs, and connecting databases from backend or API to HTML. Additionally, it covers the deployment of the project on AWS to ensure it runs continuously 24/7.

![Project Screenshot](https://github.com/miro789/LittleLemon/blob/main/littlelemon/restaurant/static/restaurant/img/poster.png)

## Features
- **User Authentication**:
  - Login: [Admin Login](http://3.106.122.33:8888/admin/login/?next=/admin/)
    - Username: `hihi`
    - Password: `123456`
  - Securing the App by Token: [API Token Auth](http://3.106.122.33:8888/api/menu/api-token-auth/)

- **Main Pages**:
  - Home: [Home Page](http://3.106.122.33:8888/restaurant/)
  - Menu: [Menu List](http://3.106.122.33:8888/restaurant/menu/)
  - Booking: [Booking Page](http://3.106.122.33:8888/restaurant/booking/)

- **Database**: MySQL

- **APIs**:
  - **API Documentations**: [API Docs](http://3.106.122.33:8888/apidocs/)
  - **Django REST Framework**:
    - Booking API: [Booking API](http://3.106.122.33:8888/api/v1/booking/tables/)
    - Menu API: [Menu API](http://3.106.122.33:8888/api/v1/menu/)

## Tools and Technologies
- **Django Framework**: For building the backend and APIs.
- **Django REST Framework**: To build Menu API and Booking API.
- **MySQL**: Used as the database.
- **Insomnia**: Used to check the API server.
- **AWS EC2**: For deployment, ensuring the project runs continuously 24/7.
- **Virtual Environment**: Using `venv` to manage dependencies.

### Folders
```
.
.
├── venv
├── manage.py
├── littlelemon (project)
│   ├── __pycache__
│   ├── tests
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── restaurant (app)
│   ├── __pycache__
│   ├── migrations
│   ├── static
│   │   ├── CSS
│   │   ├── images
│   ├── templates
│   │   ├── base.html
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── index.html
│   │   ├── booking.html
│   │   ├── menu_list.html
│   │   ├── apidocs.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
├── README.md
└── requirements.txt
```


