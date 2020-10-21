from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    catagory = models.CharField(max_length=200, blank=True, default="")
    played = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField(auto_now_add=True)
