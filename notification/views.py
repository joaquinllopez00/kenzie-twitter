from django.shortcuts import render
from notification.models import Notification
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def notification_view (request):
  notis = Notification.objects.filter(username=request.user)
  not_viewed = notis.filter(viewed=False)
  print(not_viewed)
  for x in not_viewed:
    x.viewed = True
    x.save()
  return render(request, "notification.html", {'notis': not_viewed})