![Contact Board Banner Image](/landingpage/static/landingpage/images/Github_header.png)
<h2 align='center'>Contact Board</h2>

This project is a functional web applicaction in Python and Django. This project has two applicactions. The first one is an backoffice where we can create and manage a contact list, update and/or delete them. There is also a website for an Ebook. The contacts from the form of the website will be saved in the same dababase of the backoffice.

The app Backoffice of this project was created following the project Agenda of the Udemy couse Curso de Python 3 do básico ao avançado - com projetos reais.

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
+ Css
