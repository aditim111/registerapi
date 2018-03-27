from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Hi(models.Model):
	sender = models.ForeignKey(User, related_name="sender", null=True)
	receiver = models.ForeignKey(User, related_name="receiver")
	date = models.DateTimeField(auto_now_add=True)

    