from datetime import datetime

from django.db import models

from django.utils.datetime_safe import datetime

from django.utils import timezone



class Trainingsch(models.Model):

    Trainingcode = models.IntegerField(default=0)

    Trainingtitle = models.CharField(max_length=200)

    Trainingduration = models.IntegerField(default=0)

    Trainingstart = models.DateField(default=timezone.now, blank=True, null=True)

    Trainingend = models.DateField(default=timezone.now, blank=True, null=True)

    Trainingvacancy = models.IntegerField(default=0)

    Trainingreq = models.BooleanField(default=False)

    Trainingcost = models.FloatField(blank=True, null=True)


    def __str__(self):

        return self.Trainingtitle



class Order(models.Model):


    RequestedTrainings = models.ForeignKey(Trainingsch, default=1, on_delete=models.SET_DEFAULT)

    created = models.DateTimeField(default=datetime.now)

    TransID = models.CharField(max_length=25, default="")

    PaymentID = models.CharField(max_length=100, default="")

    Requesteduser = models.CharField(max_length=100, default="")

