from django.shortcuts import render

# Create your views here.
def automotive(request):
    return render (request,'Services/automotive.html')

def industryauto(request):
   return render (request,'Services/industryauto.html')

def mobile(request):
   return render (request,'Services/mobile.html')

def website(request):
   return render (request,'Services/website.html')
