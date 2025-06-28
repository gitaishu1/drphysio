<<<<<<< HEAD
from django import forms

from .models import ROMtype_model


class ROMtypeform(forms.ModelForm):
    class Meta:
        model=ROMtype_model
=======
from django import forms

from .models import ROMtype_model


class ROMtypeform(forms.ModelForm):
    class Meta:
        model=ROMtype_model
>>>>>>> ca19d03 (add files)
        fields=('typename',)