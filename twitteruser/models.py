from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
  name = models.CharField(max_length=50)
  followees = models.ManyToManyField("self", symmetrical=False, related_name="followers")
  def __str__(self):
    return self.name
