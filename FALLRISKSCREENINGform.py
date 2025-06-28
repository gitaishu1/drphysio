<<<<<<< HEAD
from django import forms

from .models import FALLRISKSCREENING_model

class FALLRISKSCREENINGform(forms.ModelForm):
    class Meta:
        model=FALLRISKSCREENING_model
=======
from django import forms

from .models import FALLRISKSCREENING_model

class FALLRISKSCREENINGform(forms.ModelForm):
    class Meta:
        model=FALLRISKSCREENING_model
>>>>>>> ca19d03 (add files)
        fields=('criteriatype',)