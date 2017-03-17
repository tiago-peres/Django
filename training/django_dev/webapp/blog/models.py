from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model): #class is the table
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    
    def __unicode__(self): # __str__ in Python 3
        return self.title