from ssl import create_default_context
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User


# 標題/內文/建立時間/是否完成的時間/是否重要
# char/text/datetime/datetime/bool
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.title}({self.user.username})'
