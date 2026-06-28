from django.contrib import admin
from . models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display=('id','name','created_at')
    search_fields=('name',)