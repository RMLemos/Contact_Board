from landingpage import views
from django.urls import path

app_name = 'landingpage'

urlpatterns = [
    path('', views.home, name='home'),
    path('sent-ebook/', views.sent_ebook, name='sent'),
    path('terms-conditions/', views.terms, name='terms'),
]