from django.db import models
from django.contrib.auth.models import User

class ContactProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True,blank=True)
    email = models.CharField(max_length=200, null=True,blank=True)
    phone = models.IntegerField()
    message = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.name