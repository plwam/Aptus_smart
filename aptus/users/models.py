
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.hashers import make_password,check_password

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError("l'email est obligatoire.")
        email= self.normalize_email(email)
        user= self.model(email=email,**extra_fields)
        user.set_password(password)

        user.save(using= self._db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)
    
    def __str__(self):
        return self.email
  

class Users(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField( unique=True)
    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30,blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects =CustomUserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['first_name','last_name']

    class Meta:
        db_table='users.users'
    
    def __str__(self):
        return self.email
  

    def set_password(self, raw_password):
        self.password=make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password,self.password)

class Favorite(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey('library.Book', on_delete=models.CASCADE,related_name='favorited_by')
    added_at= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user
