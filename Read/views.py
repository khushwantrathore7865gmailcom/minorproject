from pyexpat.errors import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from User.models import Users
from .forms import SignUpForm
# Create your views here.
from django.views import View
import urllib.request
from bs4 import BeautifulSoup


class SignUpView(View):
    form_class = SignUpForm

    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(Users.objects.all())
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            emaill = form.cleaned_data['email']
            if Users.objects.filter(email=emaill).exists():

                return HttpResponse('User with same email already exists, Please try again with different Username!!')
            else:
                user = form.save(commit=False)
                user.username = user.email
                user.user_name = user.email
                user.is_active = True  # change this to False after testing
                user.save()

                return redirect('Read:Read/login')
                # return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


def Login(request):
    if request.user.is_authenticated:
        print(request.user)
        return redirect('Read:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            # print(username)
            # print(password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Read:home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


@login_required(login_url='/login')
def Home(request):
    user = request.user
    print(user.ApiKey)
    datafromwebsite = urllib.request.urlopen(user.ApiKey)
    select = repr(datafromwebsite.read())
    print(select)
    return render(request, 'home.html',{'content':select})


def Index(request):
    return render(request, 'index.html')
