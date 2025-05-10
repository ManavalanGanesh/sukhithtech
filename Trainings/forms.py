from django import forms

from .models import Trainingsch



class trainingschForm(forms.ModelForm):

    class Meta:

        model = Trainingsch

        fields = ["Trainingcode", "Trainingtitle", "Trainingduration", "Trainingstart", "Trainingend",

                  "Trainingvacancy", "Trainingreq", "Trainingcost"]



class Trainingreqform(forms.Form):

    TrainingReq=forms.BooleanField(initial=False)
