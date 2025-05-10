from django.db import models

class userlog(models.Model):

    firstname = models.CharField(max_length=25, default='Name')

    lastname = models.CharField(max_length=25, default='Name')

    password1 = models.CharField(max_length=25, default='PW1')

    password2 = models.CharField(max_length=25, default='Confirm')

    usrphone = models.TextField(default='934')

    username = models.CharField(max_length=25, default='Name')

