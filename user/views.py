from django.shortcuts import render

# Create your views here.
def fnmaster (request):
    return render (request,'master.html')
def fnhome (request):
    return render (request,'home.html')
def fnabtus (request):
    return render (request,'aboutus.html')
def fnstays (request):
    return render (request,'ourstays.html')