from django.shortcuts import render, redirect
from .models import Problem
from django.contrib.auth.decorators import login_required
from .forms import ProblemForm, SubmissionForm
from django.http import JsonResponse
from compiler.views import execute
import os
import json

# Create your views here.
def run(code, cinput, language):
    """
    run, ctestcase, submit the code using a compiler app.

    """
    result = execute(language, code, cinput)
    return result

def evaluate_submission(code, language, testcases, pid):
    """
    Evaluates the user's code against a set of test cases.
    Returns a dictionary with the evaluation result.
    """
    for i, testcase in enumerate(testcases):
        try:
            # The input from the JSON file needs to be serialized back to a string
            # that the executed code can read from stdin.
            input_parts = []
            for key, value in testcase['input'].items():
                if isinstance(value, list):
                    input_parts.append(' '.join(map(str, value)))
                else:
                    input_parts.append(str(value))
            cinput = '\n'.join(input_parts)

            expected_output = str(testcase['output']).lower()

        except KeyError:
            return {
                'status': f"{pid}; Invalid test case format: 'input' or 'output' key missing in testcase {i+1}.",
                'cerror': "Invalid test case format."
            }

        result = run(code, cinput, language)
        coutput = result.get("coutput", "").strip().lower()
        cerr = result.get("cerr", "").strip()

        if cerr:
            return {
                'cerror': cerr + f" (Testcase {i+1}| {cinput} : {expected_output} ~ {coutput})",
                'status': f"{pid}; Error in testcase {i+1}: {cerr}"
            }

        if coutput != expected_output:
            return {
                'cerror': f"Testcase {cinput} : {coutput}",
                'status': f"{pid}; Testcase {i+1} failed: expected '{expected_output}', got '{coutput}'"
            }

    return {'status': "Accepted!"}

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
            language = form.cleaned_data['language']
            
            if action == 'submit':
                testcase_file = os.path.join('testcases', f'{pid}.json')
                
                try:
                    with open(testcase_file, 'r') as f:
                        testcases = json.load(f)
                    
                    evaluation_result = evaluate_submission(code, language, testcases, pid)
                    ctx.update(evaluation_result)
                    
                    problem.submissions += 1
                    problem.save()

                except FileNotFoundError:
                    ctx['status'] = f"{pid}; Test cases not found for this problem."
                except json.JSONDecodeError:
                    ctx['status'] = f"{pid}; Invalid test case format."

            elif action == 'run' or action == 'testcase':
                cinput = form.cleaned_data.get('cinput', '')
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

            testcases = form.cleaned_data.get('testcases')
            
            testcase_file = os.path.join('testcases', f'{problem.id}.json')

            with open(testcase_file, 'w') as f:
                f.write(testcases)

            return redirect('problem_detail', pid=problem.id)
        
    else:
        form =  ProblemForm()
    
    return render(request, 'problem/create_problem.html', {'form': form})