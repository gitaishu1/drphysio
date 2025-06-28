<<<<<<< HEAD
from django import forms

from .models import ROM_model
class ROMform(forms.ModelForm):
    normal = forms.IntegerField(label="Normal (in degrees)", initial=50)
    left= forms.IntegerField(label="Left (in degrees)")
    right= forms.IntegerField(label="Right (in degrees)")
    class Meta:
        model=ROM_model
=======
from django import forms

from .models import ROM_model
class ROMform(forms.ModelForm):
    normal = forms.IntegerField(label="Normal (in degrees)", initial=50)
    left= forms.IntegerField(label="Left (in degrees)")
    right= forms.IntegerField(label="Right (in degrees)")
    class Meta:
        model=ROM_model
>>>>>>> ca19d03 (add files)
        fields=('typename','motionname','normal','left','right')