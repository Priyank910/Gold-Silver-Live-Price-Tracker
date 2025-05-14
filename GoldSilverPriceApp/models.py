from django.db import models

# Create your models here.
class signup(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  username = models.TextField()
  password = models.CharField(max_length=50)