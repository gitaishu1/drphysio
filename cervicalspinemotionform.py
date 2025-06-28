<<<<<<< HEAD
from django import forms

from .models import cervicalspinemotion_model
class cervicalspinemotionform(forms.ModelForm):
    class Meta:
        model=cervicalspinemotion_model
=======
from django import forms

from .models import cervicalspinemotion_model
class cervicalspinemotionform(forms.ModelForm):
    class Meta:
        model=cervicalspinemotion_model
>>>>>>> ca19d03 (add files)
        fields=('motionname','typename',)