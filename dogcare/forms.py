from django import forms
from .models import DogCarePost, Comment  

class DogCarePostForm(forms.ModelForm):
    class Meta:
        model = DogCarePost
        fields = [
            'post_type',
            'title',
            'content',
            'location',
            'date_from',
            'date_to',
            'image',
        ]
        widgets = {
            'post_type': forms.RadioSelect(choices=DogCarePost.POST_TYPE_CHOICES),
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }

# Form for comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...'
            }),
        }