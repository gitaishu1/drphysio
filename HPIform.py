<<<<<<< HEAD
from django import forms

from .models import HPI_model
class HPIform(forms.ModelForm):
    class Meta:
        model=HPI_model
=======
from django import forms

from .models import HPI_model
class HPIform(forms.ModelForm):
    class Meta:
        model=HPI_model
>>>>>>> ca19d03 (add files)
        fields=('onset','current_date','painscore','Duration','POS','Aggr','Relf')