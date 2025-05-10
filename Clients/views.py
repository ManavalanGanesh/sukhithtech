from django.shortcuts import render

# Create your views here.
def clients(request):
	return render(request,'Clients/client.html')
