from backoffice import views
from django.urls import path

app_name = 'backoffice'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]