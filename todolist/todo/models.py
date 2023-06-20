from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['completed']