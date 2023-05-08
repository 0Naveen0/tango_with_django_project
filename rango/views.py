from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict={'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    #return HttpResponse("This is your first view created in Django !!!")
    return render(request,'rango/index.html',context=context_dict)

def about(request):
    context_dict={'boldmessage':"This is about page...."}
    #return HttpResponse('This is about Page....')
    return render(request,'rango/about.html',context=context_dict)