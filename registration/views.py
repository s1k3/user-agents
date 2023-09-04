from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from user_agents import parse
from user_agent_information.models import UserAgentInformation
from django.urls import reverse
from .forms import RegisterUserForm

def index(request):
    template = loader.get_template("registration/index.html")
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name'];
            last_name = request.POST['first_name'];
            username = request.POST['username'];
            email = request.POST['email'];
            password = request.POST['password'];
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect("/")
        else:
            return HttpResponse(template.render({'message': '', 'form': form}, request))
    return HttpResponse(template.render({'message': ''}, request))

