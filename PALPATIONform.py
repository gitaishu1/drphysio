<<<<<<< HEAD
from django import forms

from .models import PALPATION_model
class PALPATIONform(forms.ModelForm):
    class Meta:
        model=PALPATION_model
=======
from django import forms

from .models import PALPATION_model
class PALPATIONform(forms.ModelForm):
    class Meta:
        model=PALPATION_model
>>>>>>> ca19d03 (add files)
        fields=('tenderness','swelling','muscletone')