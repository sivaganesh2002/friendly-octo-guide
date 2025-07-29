from django.shortcuts import render, redirect
from .models import Problem
from django.contrib.auth.decorators import login_required
from .forms import ProblemForm, SubmissionForm
from django.http import JsonResponse

# Create your views here.
def run(code, cinput, language):
    """
    run, ctestcase, submit the code using a compiler app.

    """
    
    pass

@login_required
def p_detail(request, pid):
    """
    Fetch the problem details for a given problem ID and render the detail page.
    """
    try:
        problem = Problem.objects.get(id=pid)
    except Problem.DoesNotExist:
        return redirect('problem_bank')

    ctx = {'problem': problem}

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        ctx['form'] = form

        if form.is_valid():
            action = request.POST.get('action')
            code = form.cleaned_data['code']
            cinput = form.cleaned_data['cinput']
            language = form.cleaned_data['language']
            
            if action:
                result = run(code, cinput, language)

                ctx['coutput'] = result.get("coutput", "")
                ctx['cerror'] = result.get("cerr", "")
    
    else:
        ctx['form'] = SubmissionForm()
    return render(request, 'problem/problem_detail.html', ctx)

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