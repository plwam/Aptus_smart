from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='books')
    author = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    file=models.FileField(upload_to='books/')

    def __str__(self):
        return self.title
