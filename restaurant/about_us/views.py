from django.shortcuts import render

# Create your views here.

def aboutUs(request):
    return render(request, 'about_us/about_us.html')