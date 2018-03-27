from django import forms
from .models import Hi
from django.contrib.auth.models import User



class HiForm(forms.ModelForm):

	class Meta:
		model = Hi
		fields = ['receiver']



