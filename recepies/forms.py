from django import forms

from .models import Recipe

class PostForm(forms.ModelForm):
     class Meta:
         model = Recipe
         fields = [
            "title",
            "recipe",
         ]
