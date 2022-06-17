
from asyncore import read
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Familia
from django.template import Template,context

def home(request):
    familialist=Familia.objects.all()
    return render(request,"index.htm",{"familia":familialist})