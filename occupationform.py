<<<<<<< HEAD
from django import forms

from .models import occupation_model
class occupationform(forms.ModelForm):
    class Meta:
        model=occupation_model
=======
from django import forms

from .models import occupation_model
class occupationform(forms.ModelForm):
    class Meta:
        model=occupation_model
>>>>>>> ca19d03 (add files)
        fields=('occupation',)