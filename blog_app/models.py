from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        default="",
        on_delete=models.CASCADE,
        related_name='posts'
    )
    tags = TaggableManager()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    live = models.BooleanField(default=False)
    like_num = models.PositiveIntegerField(default=0);

    class Meta:
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_app:detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        get_user_model(),
        default="",
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text



class Like(models.Model):
    user =  models.ForeignKey(
        get_user_model(),
        default="",
        on_delete=models.CASCADE,
        related_name='favorite_posts'
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_posts')
    date_created = models.DateTimeField(auto_now_add=True)
