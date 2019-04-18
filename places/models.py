from django.db import models


class Places(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
