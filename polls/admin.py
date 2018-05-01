from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question) # добавляєм моделі на сторінку адміністратора
admin.site.register(Choice) # добавляєм моделі на сторінку адм

