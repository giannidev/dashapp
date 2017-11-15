# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def home_page(request):
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    return render(request,'home.html')



#def index(request):
#    return HttpResponse("Hello, world. You're at the dashapp index.")
