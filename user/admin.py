from django.contrib import admin
from user import models


class UserAdmin(admin.ModelAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['id', 'email', 'name']
    search_fields = ['id', 'name', 'email']
    readonly_fields = ['last_login']


# Register your models here.
admin.site.register(models.User, UserAdmin)
