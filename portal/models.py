from django.db import models
from . import functions


class Email(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class CyberComplaint(models.Model):
    email = models.ForeignKey(
        Email, on_delete=models.CASCADE, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=266)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.subject
