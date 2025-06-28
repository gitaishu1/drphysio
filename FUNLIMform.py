<<<<<<< HEAD
from django import forms

from .models import FUNCTIONLIM_model
class FUNLIMform(forms.ModelForm):
    class Meta:
        model=FUNCTIONLIM_model
=======
from django import forms

from .models import FUNCTIONLIM_model
class FUNLIMform(forms.ModelForm):
    class Meta:
        model=FUNCTIONLIM_model
>>>>>>> ca19d03 (add files)
        fields=('assessmentofcondition','activitiesofdailyiving',)