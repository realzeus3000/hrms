from django.db import models
from slugify import slugify
import datetime

class Announcement(models.Model):
    title = models.CharField(blank=True, max_length=100)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    create = models.DateTimeField(blank=True, default=datetime.datetime.now)


    def __str__(self):
        return self.title
