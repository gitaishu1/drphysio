<<<<<<< HEAD
from django import forms

from .models import NEUROASS_model
class NEUROASSform(forms.ModelForm):
    class Meta:
        model=NEUROASS_model
=======
from django import forms

from .models import NEUROASS_model
class NEUROASSform(forms.ModelForm):
    class Meta:
        model=NEUROASS_model
>>>>>>> ca19d03 (add files)
        fields=('reflexes','sensation','nervefunction')