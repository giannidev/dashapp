# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Metric
from .models import Measure
from .models import Event

class EventAdmin (admin.ModelAdmin):
    list_display = ('name','date')
    
class MetricAdmin (admin.ModelAdmin):
    list_display = ('name','description','frequency','modifier')
    #list_filter = ('frequency')
    
class MeasureAdmin (admin.ModelAdmin):
    list_display = ('get_metric_name','get_event_name','rawValue','value')
    
    def get_event_name(self,obj):
        return obj.event.name
    def get_metric_name(self,obj):
        return obj.metric.name
    def get_metric_description(self,obj):
        return obj.metric.description


admin.site.register(Metric, MetricAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(Event, EventAdmin)
