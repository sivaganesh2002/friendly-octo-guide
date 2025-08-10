from django.shortcuts import render
from problem.models import Problem
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def problem_bank(request):
    """
    Fetch relevent probblems and display the problem bank.
    """
    problems = list(Problem.objects.all())
    random.shuffle(problems)

    return render(request, 'problem_bank/problemset.html', {'problems': problems})