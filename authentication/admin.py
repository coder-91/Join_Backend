from django.contrib import admin
from authentication import models



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['id', 'name', 'email']


# Register your models here.
admin.site.register(models.UserProfile)