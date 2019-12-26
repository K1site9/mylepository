from django.urls import path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('header/', views.index, name='index'),
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
]