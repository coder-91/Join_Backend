from django.contrib import admin

from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'title']
    search_fields = ['id', 'users__name', 'title', 'description']
    list_filter = ['status', 'category', 'priority']


# Register your models here.
admin.site.register(Task, TaskAdmin)
