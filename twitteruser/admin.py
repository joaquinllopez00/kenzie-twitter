from django.contrib import admin
from twitteruser.models import TwitterUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
UserAdmin.fieldsets += ('Custom fields', {'fields': ['name', 'followees']}),
admin.site.register(TwitterUser, UserAdmin)