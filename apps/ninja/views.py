from django.shortcuts import render, redirect

def index(request):
    return render(request, "ninja/index.html")

def showAll(request):
    context = {
        "word" : "all"
    }
    return render(request, "ninja/ninjas.html", context)

def showOne(request, color):
    if color == 'blue' or color == 'orange' or color =='red' or color == 'purple':
        context = {
            'color': color
        }
    else:
        context = {
            'april' : True
        }
    return render(request, 'ninja/ninjas.html', context)
# Create your views here.
