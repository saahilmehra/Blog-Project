from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
modeluser=get_user_model()

class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=250, unique_for_date='publish')
    author=models.ForeignKey(modeluser, on_delete=models.CASCADE, related_name='blog_posts')
    body=models.TextField()
    published=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering=('-published',)

    def __str__(self):
        return self.title