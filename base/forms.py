from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Enter username'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password'})
        
        
        