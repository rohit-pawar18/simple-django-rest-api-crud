from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner')


class Comments(models.Model):
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commented_user')
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='comment')
