from django.contrib import admin

from task.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'title']
    search_fields = ['id', 'contacts__name', 'title', 'description']
    list_filter = ['status', 'category', 'priority']

    #def get_contact_id(self, obj):
    #    return obj.contacts.id
    #get_contact_id.short_description = 'Contact ID'
    #get_contact_id.admin_order_field = 'contact__id'

# Register your models here.
admin.site.register(Task, TaskAdmin)