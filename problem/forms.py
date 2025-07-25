from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = [
            'title',
            'tags',
            'description',
            'difficulty',
            'constraints',
            'examples',
            'hints'
        ]

        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Comma-separated tags'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'the array of size n is...'}),
            'constraints': forms.Textarea(attrs={'rows': 3}),
            'examples': forms.Textarea(attrs={'rows': 3}),
            'hints': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['constraints'].widget.attrs.update({'class': 'form-control'})
        self.fields['examples'].widget.attrs.update({'class': 'form-control'})
        self.fields['hints'].widget.attrs.update({'class': 'form-control'})
        self.fields['difficulty'].widget = forms.Select(choices=[
            ('Easy', 'Easy'),
            ('Medium', 'Medium'),
            ('Hard', 'Hard')
        ])

        self.fields['constraints'].required = False
        self.fields['examples'].required = False
        self.fields['hints'].required = False
        
        


