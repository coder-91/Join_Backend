from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


# Register your models here.
admin.site.register(Contact, ContactAdmin)
