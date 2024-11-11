from django import forms
from .models import GuideDesc
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category"

     class Meta:    
          model = GuideDesc
          fields = ['title', 'category', 'image', 'description']
          widgets = {
               'title': forms.TextInput(attrs={'class':'create_input', 'placeholder':'Title'}),
               'category': forms.Select(attrs={'class':'create_category'}),
               'description': forms.Textarea(attrs={'class':'create_description', 'placeholder':'Description...', 'rows':4}) 
          }



class UserForm(UserCreationForm):
     class Meta:
          model = User
          fields = ["username", "email", "password1", "password2"]
          widgets = {
               'username': forms.TextInput(attrs={'placeholder': 'Username'}),
               'email': forms.EmailInput(attrs={'placeholder': 'E-mail'})
          }