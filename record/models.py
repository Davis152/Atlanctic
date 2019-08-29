from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):

    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    program=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.name + ' ' + self.last_name
