<<<<<<< HEAD
from django import forms

from .models import SPTE_model
class SPTEform(forms.ModelForm):
    class Meta:
        model=SPTE_model
=======
from django import forms

from .models import SPTE_model
class SPTEform(forms.ModelForm):
    class Meta:
        model=SPTE_model
>>>>>>> ca19d03 (add files)
        fields=('testname',)