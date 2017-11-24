# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dashapp.models import Metric, Measure
import datetime

from django.http import HttpResponse

def home_page(request):
    if request.method == 'POST':
        new_measure_M1 = request.POST.get('new_measure_M1','')
        new_measure_M2 = request.POST.get('new_measure_M2','')
        #Metric.objects.create(name=new_metric_name,description='Description for M2',frequence='RELEASE')
        Measure.objects.create(metric=Metric.objects.first(),rawValue=new_measure_M1, modifier=1, date=datetime.date.today())
        Measure.objects.create(metric=Metric.objects.last(),rawValue=new_measure_M2, modifier=1, date=datetime.date.today() )
        '''last() is a very temporary solution!'''

        return redirect('/')
    
    metrics = Metric.objects.all()
    return render(request, 'home.html', {'metrics': metrics})



#def index(request):
#    return HttpResponse("Hello, world. You're at the dashapp index.")
