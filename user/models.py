import random

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    """Manager for user"""

    def create_user(self, email, name, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    avatar_color = models.CharField(max_length=7)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.avatar_color = random.choice([
                '#FF5733', '#C70039', '#900C3F', '#581845',
                '#8E44AD', '#1F618D', '#008000', '#A52A2A', '#000080'
            ])
        super().save(*args, **kwargs)

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
