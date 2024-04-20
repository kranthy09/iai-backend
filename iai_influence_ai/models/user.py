import uuid
from django.db import models
from iai_backend.models import BasicDetails


class User(BasicDetails):
    username = models.TextField()
    social_media_account_type = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    social_media_account_id = models.CharField(
        max_length=50, default=None, blank=True, null=True)
    location = models.TextField()
