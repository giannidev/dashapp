# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Metric(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
 #   FREQUENCIES = ('Release','Month','Quarter')
    FREQUENCIES = (
    ('MONTH', 'MONTH'),
    ('QUARTER', 'QUARTER'),
    ('RELEASE', 'RELEASE'),
    )
    frequence = models.CharField(max_length=20,choices=FREQUENCIES)
    
class Measure(models.Model):
    metric = models.ForeignKey(Metric)
    rawValue = models.DecimalField(max_digits=6, decimal_places=2)
    modifier = models.DecimalField(max_digits=6, decimal_places=2)
    def _get_value(self):
        return(rawValue/modifier)
    value = property(_get_value)
    date = models.DateField()
    event = models.CharField(max_length=80)