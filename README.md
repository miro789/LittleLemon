
# Django Backend Framework Project

## Overview
This project is designed to provide a hands-on experience in creating a Backend Framework and APIs using Django. It helps in understanding the working of the Django Framework, creating APIs, and connecting databases from backend or API to HTML.

To ensure robust security, the project implements token-based authentication using Django Rest Framework (DRF) and Djoser. Users must log in to obtain a unique token, which secures access to API data, guaranteeing that only authenticated users can interact with the APIs.

Furthermore, comprehensive API documentation is generated using DRF-YASG (Yet Another Swagger Generator). This tool creates detailed Swagger (OpenAPI) documentation, clearly defining API endpoints, methods, and parameters, which promotes secure and proper usage of the APIs.

![Project Screenshot](https://github.com/miro789/LittleLemon/blob/main/littlelemon/restaurant/static/restaurant/img/poster.png)

## Features
- **User Authentication**:
  - Login: 
    - Username: `miro`
    - Password: `123456`

- **Main Pages**:
  - Home Page
  - Menu
  - Booking

- **Database**: MySQL

- **APIs**:
  - **API Documentations**:
  - **Django REST Framework**:
    - Booking API
    - Menu API

## Tools and Technologies
- **Django Framework**: For building the backend and APIs.
- **Django REST Framework**: To build Menu API and Booking API.
- **Djoser**: For simplified user authentication endpoints. 
- **DRF-YASG**: For generating Swagger (OpenAPI) documentation.
- **MySQL**: Used as the database.
- **Insomnia**: Used to check the API server.
- **Virtual Environment**: Using `venv` to manage dependencies.


## Getting Started
1. Clone the repository. 
2. Create and activate a virtual environment using `venv`. 
3. Install the required dependencies using `pip install -r requirements.txt`. 
4. Set up the MySQL or APIs database and update the database settings in the Django project. 
5. Run migrations using `python manage.py migrate`. 
6. Start the development server using `python manage.py runserver`.

## Usage 
- Access the admin interface at `Admin Login` using the provided credentials. 
- Use the `Home Page` to navigate through the main pages of the project. 
- Refer to the `API Docs` for detailed API documentation.


### Reference Video
[Watch the video](https://github.com/miro789/LittleLemon/blob/main/littlelemon/restaurant/static/restaurant/videos/ref.gif)


### API Document
![ApiDocs Screenshot](https://github.com/miro789/LittleLemon/blob/main/littlelemon/restaurant/static/restaurant/img/Apidocs.png)

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
│   │   ├── videos
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
└── requirements.txt
│README.md

```


