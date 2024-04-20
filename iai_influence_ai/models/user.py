from django.db import models
from iai_backend.models import BasicDetails


class User(BasicDetails):
    username = models.TextField()
