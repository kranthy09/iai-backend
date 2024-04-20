from django.db import models
from datetime import datetime


class AbstractDetailsModel(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_updated_datetime = models.DateTimeField(auto_now=True)

