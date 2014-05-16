from django.db import models
from django.contrib.auth.models import User


class Bunk(models.Model):
    bunkFrom = models.ForeignKey(User, related_name='from')
    bunkTo = models.ForeignKey(User, related_name='to')

    bunkTime = models.DateTimeField(auto_now_add=True)
