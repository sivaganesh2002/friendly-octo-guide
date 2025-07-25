from django.shortcuts import render
from problem.models import Problem
from django.contrib.auth.decorators import login_required


# Create your views here.
def problem_bank(request):
    """
    Fetch relevent probblems and display the problem bank.
    """
    problems = Problem.objects.all()
    return render(request, 'problem_bank/problemset.html', {'problems': problems})