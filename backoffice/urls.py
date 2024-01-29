from backoffice import views
from django.urls import path

app_name = 'backoffice'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/update/', views.update, name='update'),
    path('contact/delete/', views.delete, name='delete'),
]