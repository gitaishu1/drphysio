<<<<<<< HEAD
from django import forms

from .models import PMHM_model
class PMHMform(forms.ModelForm):
    class Meta:
        model=PMHM_model
=======
from django import forms

from .models import PMHM_model
class PMHMform(forms.ModelForm):
    class Meta:
        model=PMHM_model
>>>>>>> ca19d03 (add files)
        fields=('rmc','surgeries','Injuries','medications')