from django.db import models
from datetime import datetime

class Shout(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)
    author = models.CharField(max_length=40)
    message = models.TextField()
    zip = models.CharField(max_length=15,blank=True)
    address = models.CharField(max_length=100,blank=True)
    a = models.CharField(max_length=5,blank=True)
    book = models.CharField(max_length=60,blank=True)
    branchname = models.CharField(max_length=50, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s: %s" % (self.author, self.message[:20])
        #return "%s: %s" % (self.author, self.message, self.a[:100])

class Branch(models.Model):
    branchname = models.CharField(max_length=50, blank=True)
    branchaddress = models.CharField(max_length=100,blank=True)