from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone
# Create your models here.
class Tweet (models.Model):
  content = models.CharField(max_length=30)
  tweeter = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
  created_date = models.DateTimeField('Creation Date', default=timezone.now)
