from django.forms import ModelForm
from . models import student

class studentForm(ModelForm):
    class Meta:
        model = student
        field = ["studentname","studentnumber","studentEmail","studentpass"]
        exclude = ['createdAT']
        #fields = '__all__'