from django.contrib import admin

# Register your models here.
from .models import TodoItem, History

admin.site.register(TodoItem)
admin.site.register(History)