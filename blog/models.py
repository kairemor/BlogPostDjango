from email.policy import default

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    subtitle = models.CharField(max_length=100, default="")
    content = models.TextField()
    creation_date = models.DateTimeField('date created', default=timezone.now)
    update_date = models.DateTimeField('date updated', default=timezone.now)
    views_number = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    image = models.ImageField(upload_to='postImage', blank=True)

    def __str__(self):
        return self.title + 'posted by ' + self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments',
                             on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, default="")
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    creation_date = models.DateTimeField('date created', default=timezone.now)
    update_date = models.DateTimeField('date updated', default=timezone.now)
    sup_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_comment', null=True)

    def __str__(self):
        return self.comment 




