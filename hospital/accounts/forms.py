# accounts/forms.py

from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'profile_picture',
            'username',
            'email',
            'password',
            'address_line1',
            'city',
            'state',
            'pincode',
            'user_type'
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
            
        return cleaned_data