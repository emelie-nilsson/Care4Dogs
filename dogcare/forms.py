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
    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get("date_from")
        date_to = cleaned_data.get("date_to")

        if date_from and date_to and date_to < date_from:
            self.add_error("date_to", "End date cannot be before start date.")    

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