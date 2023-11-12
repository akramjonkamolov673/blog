from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        def _init_(self,*args,**kvargs):
            super(SignUpForm,self).__init__(*args,**kvargs)
            
            for fieldname in ['username','email','password1','password2']:
                self.fields[fieldname].help_text=None

from users.models import ProfileModel

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
    def _init_(self,*args,**kvargs):
            super(UserUpdateForm,self).__init__(*args,**kvargs)

            for fieldname in ['username','email']:
                self.fields[fieldname].help_text=None
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['image']