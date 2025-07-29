from django import forms
from .models import Problem
from django.http import JsonResponse

class SubmissionForm(forms.Form):
    language = forms.ChoiceField(
        choices=[
            ('python', 'python'),
            ('C++', 'C++'),
            ('C', 'C'),
        ],
        initial='python',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    code = forms.CharField(widget=forms.Textarea(
        attrs={'id':'vi', 'class': 'form-control', 
               'rows': 10, 'cols' : 75, 
               'placeholder': 'Write your code here...'}), 
        required=True)
    cinput = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 75, 
                'placeholder': 'Input to the code...'}),
        required=False
    )

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
        
        


