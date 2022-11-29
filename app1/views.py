from django.shortcuts import render

# Create your views here.
def mani(request):
    return render(request,'mani.html')

def raju(request):
    return render(request,'raju.html')