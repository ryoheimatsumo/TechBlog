from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        default="",
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    live = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_app:detail',kwargs={'pk':self.pk})
