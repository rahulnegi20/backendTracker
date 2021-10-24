import os 

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings

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
    title=models.CharField(max_length=255,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=140)
    def save(self,*args,**kwargs):
        auto_save_current_user(self)
        super().save(*args,**kwargs)
class Submodule(models.Model):
    title=models.CharField(max_length=140)
    module=models.ManyToManyField(Module)
    #added_on=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=140)


    def save(self,*args,**kwargs):
        auto_save_aurrent_user(self)
        super().save(*args,**kwargs)
class Resource(models.Model):
    title=models.ManyToManyField(Submodule)
    url=models.URLField(max_length=500)
    
    def save(self,*args,**kwargs):
        auto_save_current_user(self)
        super().save(*args,**kwargs)

#class Category(models.Model):
    #name=models.CharField(max_length=63)

    #class Meta:
     #   verbose_name_plural='categories'
      #  ordering=['-id']
#
 #   def __str__(self)->str:
  #      return f"{self.name}"
#class Post(models.Model):
    #title=models.CharField(max_length=127)
    #content=RichTextUploadingField()
    #slug=models.SlugField(unique=True,null=True,blank=True,max_length=255)
    #timestamp=models.DateTimeField(auto_now_add=True)
    #date_updated=models.DateTimeField(auto_now_add=True)
    #author=models.ForeignKey(User,on_delete=models.CASCADE)
    #categories=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    #views=models.IntegerField(default=0)
    #likes=models.IntegerField(default=0)
    #comments=models.IntegerFiled(dafault=0)

    #class Meta:
    #   ordering=['-id']

    #def __str__(self) -> str:
     #   return f"{self.title}"
    #def save(self,*args,**kwargs):
     #   self.slug=slugify(self.title)
      #  super(Post,self).save(*args,**kwargs)
#class Like(models.Model):
 #   user=models.ManyToManyField(User,related_name='liking_user')
  #  post=models.OneToOneFiled(Post,on_delete=models.CASCADE)





