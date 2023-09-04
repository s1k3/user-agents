from django.db import models

class UserAgentInformation(models.Model):
    browser = models.TextField(max_length=500)
    os = models.CharField(max_length=500)
    device = models.CharField(max_length=500)
    is_tablet = models.BooleanField()
    is_pc = models.BooleanField()
    is_mobile = models.BooleanField()
    is_touch_capable = models.BooleanField()
    is_bot = models.BooleanField()
