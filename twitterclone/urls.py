"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tweet import views as tweetviews
from authentication import views as authviews
from twitteruser import views as userviews
from notification import views as notiviews
urlpatterns = [
    path("", tweetviews.index, name="homepage"),
    path("tweet/", tweetviews.tweet),
    path("notifications/", notiviews.notification_view),
    path("tweet/<int:tweet_id>", tweetviews.tweet_detail),
    path("user/", userviews.user_view),
    path("user/<str:user_name>", userviews.user_view),
    path("unfollow/<int:unfollowed_user>", userviews.unfollow_user),
    path("follow/<int:followed_user>", userviews.follow_user),
    path("login/", authviews.login_view, name="login"),
    path("logout/", authviews.logout_view),
    path("signup/", authviews.sign_up ),
    path('admin/', admin.site.urls),
]
