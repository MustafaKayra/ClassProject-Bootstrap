from django.contrib import admin
from .models import Person,Report

admin.site.register(Person) #Admin sayfasında Kişileri görebilmek için açılan sekme
admin.site.register(Report) #Admin sayfasında geri bildirimleri görebilmek için açılan sekme
