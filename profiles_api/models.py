from turtle import end_fill
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
# Create your models here.


class UserProfileManager(BaseUserManager, models.Manager):
    #Manager for user profiles

    def create_user(self, email, f_name, password=None):
        # Create a new user profile
        if not email:
            raise ValueError('Users must have an E-Mail address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=f_name)

        user.make_password(password)
        user.save(using=self._db)
        

        return user

    def create_superuser(self, email, f_name, password):

        user = self.create_user(email, f_name, password)
        user.is_superuser = True
        user.is_staff = True


class UserProfile(AbstractBaseUser, PermissionsMixin, models.Model):
    #database model for users in the system

    email = models.EmailField(unique=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #this will replace the default username with email in authentication
    REQUIRED_FIELDS = ['f_name', 'l_name']

    def get_full_name(self):
        return self.f_name + " " + self.l_name

    def __str__(self):
        return self.email