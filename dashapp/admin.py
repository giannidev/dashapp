# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Metric
from .models import Measure

admin.site.register(Metric)
admin.site.register(Measure)