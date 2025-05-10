from django.shortcuts import render,reverse
from .models import Trainingsch

# Create your views here.
def trainings(request):
    queryset=Trainingsch.objects.all()
    context ={
               'trgsch':queryset
    }
    return render(request,'Trainings/trainings.html',context)
