from django.contrib import admin
from .models import *


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('title_en', 'title_cz')


@admin.register(Emails)
class Email(admin.ModelAdmin):
    list_display = ('name', 'email')


