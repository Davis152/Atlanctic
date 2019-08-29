from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ExtendedUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
   # first_name = forms.CharField(max_length=50)
   # last_name = forms.CharField(max_length=50)
   # email2 = forms.ModelMultipleChoiceField(queryset=User.objects.all(),empty_label=None)
   # typeuser = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="Choose", label='Type User')
   # is_staff = forms.CheckboxInput(label="Is Employeer")

    class Meta:
        model = User
        # fields = ('username','email','first_name','last_name','password1','password2')
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
          #user.firt_name = self.cleaned_data['firt_name']
           #user.last_name = self.cleaned_data['last_name']
            if commit:
                    user.save()
            return user

class UserProfileForm(forms.ModelForm):
    class Meta:
            model = Profile
            fields = ('typeuser',)

        # fields = ('typeuser', 'suscription', 'country')

class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()

        class Meta:
            model = User
            fields = ['email',]
            #fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

        class Meta:
            model = Profile
            fields = ['image']