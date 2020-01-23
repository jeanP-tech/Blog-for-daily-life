from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    secret = models.BooleanField(default=False)

    class Meta:
        permissions = (("can_post", "can post"),)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
