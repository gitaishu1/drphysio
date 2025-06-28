<<<<<<< HEAD
from django import forms

from .models import MMTmotion_model
class MMTmotionform(forms.ModelForm):
    class Meta:
        model=MMTmotion_model
=======
from django import forms

from .models import MMTmotion_model
class MMTmotionform(forms.ModelForm):
    class Meta:
        model=MMTmotion_model
>>>>>>> ca19d03 (add files)
        fields=('typename','motionname',)