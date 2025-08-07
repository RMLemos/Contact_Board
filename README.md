![Contact Board Banner Image](/landingpage/static/landingpage/images/github_header.png)
<h2 align='center'>Contact Board</h2>

This project is a functional web application developed in Python and Django. This project consists of two applications. The first one is a backoffice where users can create and manage a contact list, as well as update and delete contacts. The second is a website for an Ebook. The contacts submitted through the website's form are saved in the same database as the backoffice.

### Contact Board Main Page
![Contact Board main Image](/landingpage/static/landingpage/images/contact_manager.png)

### Landing Page Main Page
![Landingpage main Image](/landingpage/static/landingpage/images/landingpage.png)


### Usage

1. After cloning this repository, create a virtual environment and install the requirements listed in the 'requirements.txt' file:

```
pip install -r requirements.txt
```

2. In the file setting.py, configure the database settings.
3. Execute below commands:

```
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser for admin access and follow instructions:

```
python manage.py createsuperuser
```

5. Running the tests
   
```
python manage.py runserver
```

### Tools
+ Django
+ Laragon
+ MySQL
+ Python
+ Html
+ CSS

References:
+ Agenda of the Udemy couse Curso de Python 3 do básico ao avançado - com projetos reais
