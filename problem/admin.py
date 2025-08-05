from django.contrib import admin
from . import models, forms
import os

class ProblemAdmin(admin.ModelAdmin):
    form = forms.ProblemForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        # Save input and output files if provided
        testcases = form.cleaned_data.get('testcases')

        if testcases:
            # Ensure the testcases directory exists
            if not os.path.exists('testcases'):
                os.makedirs('testcases')

            testcases_file = os.path.join('testcases', f'{obj.id}.json')

            with open(testcases_file, 'w') as f:
                f.write(testcases)


admin.site.register(models.Problem, ProblemAdmin)