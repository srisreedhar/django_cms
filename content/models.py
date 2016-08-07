from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=30)
    body = models.TextField()
    
