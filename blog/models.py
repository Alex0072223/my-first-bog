# coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class POST(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title
