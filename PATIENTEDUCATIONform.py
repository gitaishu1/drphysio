<<<<<<< HEAD
from django import forms

from .models import PATIENTEDUCATION_model
class PATIENTEDUCATIONform(forms.ModelForm):
    class Meta:
        model=PATIENTEDUCATION_model
=======
from django import forms

from .models import PATIENTEDUCATION_model
class PATIENTEDUCATIONform(forms.ModelForm):
    class Meta:
        model=PATIENTEDUCATION_model
>>>>>>> ca19d03 (add files)
        fields=('explanationofcondition','prognosis','selfmanagement')