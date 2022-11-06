from django import forms
from . import models
from django.contrib.auth.models import User



class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend docto
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=User.objects.all().filter(groups__name='TEACHER'),empty_label="Name and Department", to_field_name="id")
    class Meta:
        model=models.Patient
        fields=['mobile','status','symptoms','partiality','loud','clarity','punctual','time','sub']


