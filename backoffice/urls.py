from backoffice import views
from django.urls import path

app_name = 'backoffice'

urlpatterns = [
    path('', views.index, name='index'),
]