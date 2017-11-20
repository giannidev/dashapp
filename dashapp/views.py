# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from dashapp.models import Metric

from django.http import HttpResponse

def home_page(request):
    if request.method == 'POST':
        new_metric_name = request.POST.get('new_metric','')
        new_measure = request.POST.get('new_measure')
        #Metric.objects.create(name=new_metric_name,description='Description for M2',frequence='RELEASE')
        Metric.objects.create(name=new_metric_name)
    else:
        new_metric_name =''
        new_measure =''
    
    return render(request, 'home.html', {
        'new_metric': request.POST.get('new_metric',''),
        'new_measure': request.POST.get('new_measure',''),
    })



#def index(request):
#    return HttpResponse("Hello, world. You're at the dashapp index.")
