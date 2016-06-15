from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class AreaChief(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    