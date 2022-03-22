from audioop import maxpp
from statistics import mode
from sunau import AUDIO_FILE_ENCODING_DOUBLE

from django import forms
from django.db import models


class Phase(models.Model):
    spectrum=models.CharField(max_length=100)
    base_price=models.DecimalField(decimal_places=2, max_digits=100)
    no_of_blocks=models.IntegerField()

class Round(models.Model):
    phase=models.IntegerField()
    actionStatus=models.BooleanField(default=False)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

class BidderInfo(models.Model):
    designation=models.CharField(max_length=100)
    organization=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    company=models.CharField(max_length=100)

class AuctionDetails(models.Model):
    spectrum=models.CharField(max_length=100)
    base_price=models.DecimalField(decimal_places=2, max_digits=100)
    round_number=models.IntegerField()
    no_of_block=models.IntegerField()



class Auction(models.Model):
    round=models.ForeignKey(Round, on_delete=models.CASCADE)
    auc_status=models.BooleanField(default=False)
    start_time=models.DateTimeField()
