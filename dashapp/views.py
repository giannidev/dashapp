# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dashapp.models import Metric, Measure, Event
from datetime import date

from django.http import HttpResponse

def home_page(request):
    if request.method == 'POST':
        new_measure_M1 = request.POST.get('new_measure_M1','')
        new_measure_M2 = request.POST.get('new_measure_M2','')
        new_event_name = request.POST.get('new_event_name','')
        
        '''Create and store the event'''
        Event.objects.create(name=new_event_name, date=date.today())
        
        '''Create and store the measures'''
        Measure.objects.create(metric=Metric.objects.first(), rawValue=new_measure_M1, event=Event.objects.first())
        Measure.objects.create(metric=Metric.objects.last(), rawValue=new_measure_M2, event=Event.objects.first())
        ''' TODO
            1)The event has to be created in the DB before adding a measure'''

        return redirect('/')
    
    metrics = Metric.objects.all()
    return render(request, 'home.html', {'metrics': metrics})



#def index(request):
#    return HttpResponse("Hello, world. You're at the dashapp index.")
