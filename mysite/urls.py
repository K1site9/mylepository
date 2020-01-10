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
    path('techskill/java/access/', views.javaaccess, name='javaaccess'),
    path('techskill/java/generic/', views.javageneric, name='javageneric'),
    path('techskill/java/collection/', views.javacollection, name='javacollection'),
    path('techskill/java/exception/', views.javaexception, name='javaexception'),
    path('techskill/java/ramuda/', views.javaramuda, name='javaramuda'),
]