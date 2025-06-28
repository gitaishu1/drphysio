<<<<<<< HEAD
from django import forms

from .models import complaint_model
class complaintform(forms.ModelForm):
    class Meta:
        model=complaint_model
=======
from django import forms

from .models import complaint_model
class complaintform(forms.ModelForm):
    class Meta:
        model=complaint_model
>>>>>>> ca19d03 (add files)
        fields=('complaint','name',)