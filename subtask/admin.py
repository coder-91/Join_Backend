from django.contrib import admin

from subtask.models import Subtask


class SubtaskAdmin(admin.ModelAdmin):
    def get_task_id(self, obj):
        return obj.task.id

    list_display = ['id', 'get_task_id', 'is_done', 'description']
    search_fields = ['id', 'task__id', 'description']
    list_filter = ['is_done']
    get_task_id.short_description = 'Task ID'


# Register your models here.
admin.site.register(Subtask, SubtaskAdmin)
