from django.http import HttpResponse
from django.template import loader

from user_agent_information.models import UserAgentInformation

def index(request):
    agents = UserAgentInformation.objects.all()
    template = loader.get_template("user_agents/index.html")
    return HttpResponse(template.render({'agents': agents}, request))
