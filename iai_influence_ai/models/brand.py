from django.db import models
from .user import User


class Brand(models.Model):
    user = models.ForeignKey(User)
    official_name = models.TextField()
    category = models.TextField()
