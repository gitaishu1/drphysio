<<<<<<< HEAD
from django import forms

from .models import SocialHistory_model
class socialhistoryform(forms.ModelForm):
    class Meta:
        model=SocialHistory_model
=======
from django import forms

from .models import SocialHistory_model
class socialhistoryform(forms.ModelForm):
    class Meta:
        model=SocialHistory_model
>>>>>>> ca19d03 (add files)
        fields=('lifestyle','activitylevels','habits','healthissues')