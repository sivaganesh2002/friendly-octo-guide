from django import forms
from .models import Problem
from django.http import JsonResponse

class SubmissionForm(forms.Form):
    language = forms.ChoiceField(
        choices=[
            ('py', 'python'),
            ('cpp', 'C++'),
            ('c', 'C'),
        ],
        initial='python',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    code = forms.CharField(widget=forms.Textarea(
        attrs={'id':'vi', 'class': 'form-control', 
               'rows': 10, 'cols' : 75, 
               'placeholder': 'print("Hello World")'}), 
        required=True)
    cinput = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 75, 
                'placeholder': 'Input to the code...'}),
        required=False
    )

class ProblemForm(forms.ModelForm):
    testcases = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 20, 'cols': 25, 
                'placeholder': 'Input to the testcase json...'
               }),
        label='Testcase json',
    )

    class Meta:
        model = Problem
        fields = [
            'title',
            'tags',
            'description',
            'difficulty',
            'constraints'
        ]

        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Comma-separated tags'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'the array of size n is...'}),
            'constraints': forms.Textarea(attrs={'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['constraints'].widget.attrs.update({'class': 'form-control'})
        self.fields['difficulty'].widget = forms.Select(choices=[
            ('Easy', 'Easy'),
            ('Medium', 'Medium'),
            ('Hard', 'Hard')
        ])
        self.fields['testcases'].widget.attrs.update({'class': 'form-control'})

        self.fields['constraints'].required = False

        