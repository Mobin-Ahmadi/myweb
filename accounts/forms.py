from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید رمز', widget=forms.PasswordInput)
    email = forms.EmailField(label='ایمیل', required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("رمزها مطابقت ندارند")
        return self.cleaned_data['password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            
        return user