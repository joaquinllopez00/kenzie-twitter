from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from twitteruser.models import TwitterUser
from authentication.forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def sign_up(request):
  if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['name'], 'authviews')
            finuser = TwitterUser.objects.create_user(username=data['username'],password=data['password'], name=data['name'])
        return HttpResponseRedirect(reverse('login'))
  form = CreateUserForm()
  return render(request, 'sign_up.html', {'form': form})

def login_view(request):
  if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user, "user")
            if user:
                print("if user")
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
  form = LoginForm()

  return render(request, "login.html", {'form': form})

def logout_view(request):
  user = request.user
  print(request.user)
  logout(request)
  return HttpResponseRedirect(reverse('homepage'))