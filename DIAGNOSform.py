<<<<<<< HEAD
from django import forms

from .models import DIAGNOS_model
class DIAGNOSform(forms.ModelForm):
    class Meta:
        model=DIAGNOS_model
=======
from django import forms

from .models import DIAGNOS_model
class DIAGNOSform(forms.ModelForm):
    class Meta:
        model=DIAGNOS_model
>>>>>>> ca19d03 (add files)
        fields=('Xrays','MRI','CT','lab',)