from django.shortcuts import render

# Create your views here.
def fnh (request):
    return render (request,'masteradmin.html')
def fnaddash (request):
    return render (request,'admindashboard.html')
def fnadbook (request):
    return render (request,'booking.html')
def fnadrooms (request):
    return render (request,'rooms.html')