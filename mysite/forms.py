from django import forms
from .models import Signup,userform

class SignupForm(forms.ModelForm): 
    class Meta:
        model = Signup
        fields = "__all__"
        
class Userformdata(forms.ModelForm):
    class Meta:
        model = userform
        fields = "__all__"
        
        