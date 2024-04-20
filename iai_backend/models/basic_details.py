from django.db import models
from abstract_datetime import AbstractDetailsModel


class BasicDetails(AbstractDetailsModel):
    name = models.TextField()
    pic_url = models.CharField(max_length=100)
    description = models.TextField()
