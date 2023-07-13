from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    tags = TaggableManager()