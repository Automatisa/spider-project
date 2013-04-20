from django.db import models

# Create your models here.

class Video(models.Model):
    category = models.IntegerField(default=0)
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=20, null=True, blank=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    actor = models.CharField(max_length=100, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=20, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    serial = models.CharField(max_length=20, null=True, blank=True)
    end = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    update_time = models.DateTimeField()

class Url(models.Model):
    video = models.ForeignKey(Video)
    oid = models.IntegerField(default=0)
    url_type = models.CharField(max_length=10)
    url_name = models.CharField(max_length=10, null=True, blank=True)
    url = models.CharField(max_length=200)
