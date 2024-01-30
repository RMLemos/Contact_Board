from backoffice import views
from django.urls import path

app_name = 'backoffice'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/update/', views.user_update, name='user_update'),
    path('user/logout/', views.logout_view, name='logout'),
]