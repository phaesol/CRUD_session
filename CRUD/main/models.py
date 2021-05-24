from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Write(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Write,related_name="comment",on_delete=CASCADE)
    user = models.ForeignKey(User,related_name="comment",on_delete=CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.post.title