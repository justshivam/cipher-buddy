from django.db import models


class Email(models.Model):
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.email


class Complaint(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    subject = models.CharField(max_length=266)
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.subject


class SiteComplaint(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    subject = models.CharField(max_length=266)
    details = models.CharField(max_length=1000)
    website = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.website} - {self.subject}'


class Contact(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    time = models.CharField(max_length=30)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.comments
