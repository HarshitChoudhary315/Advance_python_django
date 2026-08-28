from django.urls import path
from .import views


urlpatterns = [
    path('testors/',views.testors),
    path('display/',views.display),
    path('welcome/',views.welcome),
]