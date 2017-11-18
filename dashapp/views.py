# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('new_metric',''),
    })



#def index(request):
#    return HttpResponse("Hello, world. You're at the dashapp index.")
