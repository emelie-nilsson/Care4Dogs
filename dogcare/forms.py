from django import forms
from .models import DogCarePost

class DogCarePostForm(forms.ModelForm):
    class Meta:
        model = DogCarePost
        fields = ['title', 'content', 'post_type', 'location', 'image']
        widgets = {
            'post_type': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'rows': 4}),
        }