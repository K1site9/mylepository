from django.contrib import admin

# Register your models here.
from mysite.models import *
from django.contrib import admin

admin.site.register(Article)
admin.site.register(Question)
# admin.site.register(Heading)