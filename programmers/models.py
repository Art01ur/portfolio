from django.contrib.auth.models import User
from django.db import models


class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=20)
    framework = models.CharField(max_length=20)
    experience = models.IntegerField()

    def __str__(self):
        return self.user


class Project(models.Model):
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
