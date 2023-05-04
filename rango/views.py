from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is your first view created in Django !!!")

def about(request):
    return HttpResponse('This is about Page....')