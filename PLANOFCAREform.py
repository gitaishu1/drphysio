<<<<<<< HEAD
from django import forms

from .models import PLANOFCARE_model
class PLANOFCAREform(forms.ModelForm):
    class Meta:
        model=PLANOFCARE_model
=======
from django import forms

from .models import PLANOFCARE_model
class PLANOFCAREform(forms.ModelForm):
    class Meta:
        model=PLANOFCARE_model
>>>>>>> ca19d03 (add files)
        fields=('treatmentstrategies','modalities','exercises')