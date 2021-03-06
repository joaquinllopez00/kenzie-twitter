from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
@login_required
def user_view(request, user_name: str=""):
  following = 0
  for user in TwitterUser.objects.all():
    if request.user in user.followees.all():
      following += 1
  print(following)
  if user_name == "" or user_name == request.user.username:
    if request.user:
      user = request.user
      tweets = Tweet.objects.filter(tweeter=user)
      count = tweets.count()
      print(count)
    else:
      return HttpResponseRedirect("/login")
    return render(request, 'user_detail.html', {'user': user, 'tweets': tweets, 'count': count, "userpage": True, "following": following})
  user = TwitterUser.objects.get(username=user_name)
  tweets = Tweet.objects.filter(tweeter=user)
  count = tweets.count()
  followees = user.followees.all()
  # follow = TwitterUser.objects.filter(followees =user)
  if request.user in followees:
    print("included")
    follow = True
  else:
    follow = False
  
  print(followees, follow, request.user, count)
  return render(request, "user_detail.html", {'user': user, 'tweets': tweets, 'count': count,'follow': follow, "userpage": False, "following": following}, )


def follow_user(request, followed_user:int):
  print(followed_user, "int")
  follow_user = TwitterUser.objects.get(id=followed_user)
  print(follow_user, "user we are trying to folllow")
  following_user = request.user
  follow_user.followees.add(following_user)
  follow_user.save()
  print(follow_user.followees.count(), "user_request", following_user,"request.user")
  return HttpResponseRedirect("/user/%s" % follow_user.username)

def unfollow_user(request, unfollowed_user:int):
  unfollow_user = TwitterUser.objects.get(id=unfollowed_user)
  unfollowing_user = request.user
  unfollow_user.followees.remove(unfollowing_user)
  unfollow_user.save()
  return HttpResponseRedirect("/user/%s" % unfollow_user.username
  )