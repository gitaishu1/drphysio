<<<<<<< HEAD
from django import forms

from .models import IMPRESSION_model
class IMPRESSIONform(forms.ModelForm):
    class Meta:
        model=IMPRESSION_model
=======
from django import forms

from .models import IMPRESSION_model
class IMPRESSIONform(forms.ModelForm):
    class Meta:
        model=IMPRESSION_model
>>>>>>> ca19d03 (add files)
        fields=('summary','provisionaldiagnos',)