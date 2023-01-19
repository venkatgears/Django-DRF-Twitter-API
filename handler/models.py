from django.db import models

# Create your models here.


class Twitter_Profiles(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=500, null=False, blank=False, unique=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    profile_image_url = models.URLField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.username
