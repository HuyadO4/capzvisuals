#from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField(max_length=2080)
    #created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    #id = models.UUIDField(null=True)

    #class Meta:
    #    ordering = ['-created']

    def __str__(self):
        return self.message




class Beauty(models.Model):
    #username = models.CharField(max_length=300, null=True)
    #message = models.CharField(max_length=230, null=True)
    #sample_chapter = models.FileField(blank=True, null=True, upload_to='beauty/%Y/%m/%D/' )
    image = models.ImageField(null=True, blank=True, upload_to='beauty/')

class Birthday(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='birthday/')

class Event(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='event/')

class Fashion(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='fashion/')

class Wedding (models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='wedding/')
