from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def product(request):
    return render(request,"products.html")

def contact(request):
    return render(request,"contactus.html")