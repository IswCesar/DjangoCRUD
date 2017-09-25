# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.address + " " + self.email

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email