# Models
from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length = 200)
	content = models.TextField()
	created = models.DateTimeField(default=timezone.now) 