from django.db import models


class Tweets(models.Model):
    text = models.CharField(max_length=70, blank=False, default='')
    label = models.CharField(max_length=200,blank=False, default='')
 

