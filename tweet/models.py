from django.db import models
from twitteruser.models import TwitterUser
# Create your models here.
class Tweet (models.Model):
  content = models.CharField(max_length=30)
  tweeter = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)