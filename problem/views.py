from django.shortcuts import render, redirect
from .models import Problem
from django.contrib.auth.decorators import login_required
from .forms import ProblemForm

# Create your views here.
@login_required
def p_detail(request, pid):
    """
    Fetch the problem details for a given problem ID and render the detail page.
    """
    try:
        problem = Problem.objects.get(id=pid)
    except Problem.DoesNotExist:
        return redirect('problem_bank')
    return render(request, 'problem/problem_detail.html', {'problem': problem})

@login_required
def create_problem(request):
    """
    Handle the creation of a new problem.
    """
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.creator = request.user
            problem.save()
            return redirect('problem_detail', pid=problem.id)
    else:
        form =  ProblemForm()
    
    return render(request, 'problem/create_problem.html', {'form': form})