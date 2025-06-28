<<<<<<< HEAD
from django import forms

from .models import objectiveassessment_model
class objectiveassessmentform(forms.ModelForm):
    class Meta:
        model=objectiveassessment_model
=======
from django import forms

from .models import objectiveassessment_model
class objectiveassessmentform(forms.ModelForm):
    class Meta:
        model=objectiveassessment_model
>>>>>>> ca19d03 (add files)
        fields=('postureandmovement',)