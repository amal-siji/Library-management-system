from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    name = models.EmailField(max_length=255, null=True)
    email = models.CharField(max_length=10000)
    message = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.name

class lr_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='li_images', null=True, blank=True)
    age = models.IntegerField()

class cu_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='li_images', null=True, blank=True)
    age = models.IntegerField()
    email = models.EmailField(null=True)

class lr_addbook(models.Model):
    bookname = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, null=True)
    bookDescription = models.TextField(null=True)
    image = models.ImageField(upload_to='bookadd', null=True, blank=True)

    def __str__(self):
        return self.bookname

class book_rent(models.Model):
    name = models.CharField(max_length=255)
    startdate = models .DateField(auto_now_add=True, null=True, blank=True)
    bookname = models.CharField(max_length=255, null=True)
    How_many_days_you_need = models.IntegerField(null=True)
    phoneno = models.CharField(max_length=10)

class li_message(models.Model):
    sender = models.CharField(max_length=255, null=True)
    reciever = models.CharField(max_length=255, null=True)
    message_content = models.TextField(max_length=255, null=True)



