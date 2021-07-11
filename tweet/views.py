from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.forms import TweetForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification
from itertools import chain
# Create your views here.

@login_required
def index(request):
  user = request.user
  user_tweets = Tweet.objects.filter(tweeter=request.user)
  # user = TwitterUser.objects.get(username=user_name)
  tweets = []
  tweets += user_tweets
  users = TwitterUser.objects.all()
  print(user.followees.all())
  for u in users:
    print(u, "users")
    if user in u.followees.all():
      print("following tweet", u)
      tweets += chain(Tweet.objects.filter(tweeter=u))
      print(tweets)
      
  fin_tweets = sorted(tweets, key= lambda tweet: tweet.created_date)
  # print(user_tweets, "tweets", user.followees, "user", tweets, "tweets")
  return render(request, 'index.html', {'user': user, 'tweets': fin_tweets[::-1]})


@login_required
def tweet(request):

  if request.method == "POST":
      form = TweetForm(request.POST)
      if form.is_valid():
          data = form.cleaned_data
          tweet = Tweet.objects.create(
              content = data['content'],
              tweeter = request.user
              )
          checkNotiStr = data['content'].split(" ")
          for index, work in enumerate(checkNotiStr):
            if work[0] == '@':
              print(work[1:], "user")
              user = TwitterUser.objects.get(username=work[1:])
              print(user, "userfound")
              noti = Notification.objects.create(content=tweet, username=user)
              print(noti)
          return HttpResponseRedirect(reverse("homepage"))
  form = TweetForm()
  return render(request, "tweet.html", {'form': form})


def tweet_detail(request, tweet_id:int=""):
  if tweet_id:
    tweet = Tweet.objects.get(id=tweet_id)
    print(tweet)
    return render(request, "tweet_detail.html", {'tweet': tweet})