from django.db import models


class Stones(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image_url = models.CharField(max_length=1083)