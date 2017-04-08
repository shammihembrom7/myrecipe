from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()
from .models import Recipe

class PostForm(forms.ModelForm):
     class Meta:
         model = Recipe
         fields = [
            "title",
            "recipe",
         ]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("This user does not exit")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
        return super(UserLoginForm, self).clean(*args,**kwargs)

class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
    def clean(self, *args, **kwargs):
        return super(UserRegForm,self).clean(*args, **kwargs)
