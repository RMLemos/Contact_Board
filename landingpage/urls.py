from landingpage import views
from django.urls import path

urlpatterns = [
    path('', views.landingpage),
]