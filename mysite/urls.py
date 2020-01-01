from django.urls import path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('header/', views.index, name='index'),
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('memo/git/', views.git, name='git'),
    path('humanskill/idea/', views.idea, name='idea'),
    path('memo/excel/', views.excel, name='excel'),
    path('techskill/java/', views.java, name='java'),
    path('techskill/java/base/', views.javabase, name='javabase'),
    path('techskill/java/const/', views.javaconst, name='javaconst'),
]