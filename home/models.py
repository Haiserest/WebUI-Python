import email
from django.db import models

# Create your models here.

class ContactMsg(models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title