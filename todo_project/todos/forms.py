from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'status']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=255, required=False)
