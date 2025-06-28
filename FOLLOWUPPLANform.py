<<<<<<< HEAD
from django import forms

from .models import FOLLOWUPPLAN_model
class FOLLOWUPPLANform(forms.ModelForm):
    class Meta:
        model=FOLLOWUPPLAN_model
=======
from django import forms

from .models import FOLLOWUPPLAN_model
class FOLLOWUPPLANform(forms.ModelForm):
    class Meta:
        model=FOLLOWUPPLAN_model
>>>>>>> ca19d03 (add files)
        fields=('frequencyofvisits','reassessment','modifications')