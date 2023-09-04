from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from user_agents import parse
from user_agent_information.models import UserAgentInformation
from .forms import LogInUser

def index(request):
    template = loader.get_template("login/index.html")
    if request.method == 'POST':
        form = LogInUser(request.POST)
        if form.is_valid():    
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.get(email=email)
            if user is not None:
                auth = authenticate(username = user.username, password = password)
                if auth is not None:
                    user_agent = parse(request.META['HTTP_USER_AGENT'])
                    UserAgentInformation(
                        browser = user_agent.browser,
                        os = user_agent.os,
                        device = user_agent.device,
                        is_tablet = user_agent.is_tablet,
                        is_pc = user_agent.is_pc,
                        is_mobile = user_agent.is_mobile,
                        is_touch_capable = user_agent.is_touch_capable,
                        is_bot = user_agent.is_bot
                    ).save()
                    return redirect('user/agents')
        else:
            return HttpResponse(template.render({'message': '', 'form': form}, request))
    return HttpResponse(template.render({'message': ''}, request))


def logoutUser(request):
    logout(request)
    return redirect('/')