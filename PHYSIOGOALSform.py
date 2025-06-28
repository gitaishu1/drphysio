<<<<<<< HEAD
from django import forms

from .models import PHYSIOGOALS_model
class PHYSIOGOALSform(forms.ModelForm):
    class Meta:
        model=PHYSIOGOALS_model
=======
from django import forms

from .models import PHYSIOGOALS_model
class PHYSIOGOALSform(forms.ModelForm):
    class Meta:
        model=PHYSIOGOALS_model
>>>>>>> ca19d03 (add files)
        fields=('shorttermgoals','longtermgoals',)