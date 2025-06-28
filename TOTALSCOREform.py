<<<<<<< HEAD
from django import forms

from .models import TOTALSCORE_model
class TOTALSCOREform(forms.ModelForm):
    class Meta:
        model=TOTALSCORE_model
=======
from django import forms

from .models import TOTALSCORE_model
class TOTALSCOREform(forms.ModelForm):
    class Meta:
        model=TOTALSCORE_model
>>>>>>> ca19d03 (add files)
        fields=('range',)