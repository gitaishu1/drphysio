<<<<<<< HEAD
from django import forms

from .models import CRITERIAsection_model
class CRITERIAsectionform(forms.ModelForm):
    class Meta:
        model=CRITERIAsection_model
=======
from django import forms

from .models import CRITERIAsection_model
class CRITERIAsectionform(forms.ModelForm):
    class Meta:
        model=CRITERIAsection_model
>>>>>>> ca19d03 (add files)
        fields=('criteriatype','sectionname',)