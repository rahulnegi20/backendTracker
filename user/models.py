import os 

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from django.http import request

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user
        """
        if not email:
            raise ValueError("Users must have an email address!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and saves a new superuser
        """
        user =self.create_user(email, password)
        user.is_staff =True 
        user.is_superuser =True 
        user.save(using=self._db)

        return user   

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that supports email instead 
    of username
    """
    email       = models.EmailField(max_length=255, unique=True)
    name        = models.CharField(max_length=255)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Module(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=140)


class Submodule(models.Model):
    title=models.CharField(max_length=140,default="")
    module=models.ForeignKey(Module,on_delete=models.CASCADE,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=140,default="")


class Resource(models.Model):
    submodule=models.ForeignKey(Submodule,on_delete=models.CASCADE,default="")
    title=models.CharField(max_length=140,default="")
    url=models.URLField(max_length=500,default="")
    created_at=models.DateTimeField(auto_now_add=True)

