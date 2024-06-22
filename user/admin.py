from django.contrib import admin
from django.contrib.auth.hashers import make_password

from user import models


class UserAdmin(admin.ModelAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['id', 'email', 'name']
    search_fields = ['id', 'name', 'email']
    readonly_fields = ['last_login']

    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        obj.user = request.user
        obj.save()


# Register your models here.
admin.site.register(models.User, UserAdmin)
