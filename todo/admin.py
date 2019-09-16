from django.contrib import admin
from .models import ToDo
# Register your models here.

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title','task_done','created','updated')
    list_filter = ('task_done',)
