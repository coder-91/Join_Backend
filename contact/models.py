from django.db import models


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    avatar_color: models.CharField(max_length=7)
