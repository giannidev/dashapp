# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Metric(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    FREQUENCIES = (
    ('MONTH', 'MONTH'),
    ('QUARTER', 'QUARTER'),
    ('RELEASE', 'RELEASE'),
    )
    frequency = models.CharField(max_length=20,choices=FREQUENCIES)
    modifier = models.DecimalField(max_digits=6, decimal_places=2, default=1)
    
class Event(models.Model):
    name = models.CharField(max_length=80)
    date = models.DateField()


class Measure(models.Model):
    metric = models.ForeignKey(Metric)
    event = models.ForeignKey(Event)
    rawValue = models.DecimalField(max_digits=6, decimal_places=2)
    
    @property
    def value(self):
        return(self.rawValue / self.metric.modifier)
