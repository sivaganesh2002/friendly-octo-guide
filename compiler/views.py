import os
from pathlib import Path
import subprocess
from django.conf import settings
import uuid

# define path to tmp directory
COMPILER_DIR = Path(settings.BASE_DIR) / 'compiler' / 'tmp'
CODE_DIR = COMPILER_DIR / 'code'
EXEC_DIR = COMPILER_DIR / 'exec'

def compile_python(path, cinput):
    """
    execute python code
    """
    process = subprocess.run(
        ['python', str(path)],
        stdin=cinput,
        stdout=process.PIPE,
        stderr=process.PIPE,
    )
    return {
        'coutput': process.stdout,
        'cerr': process.stderr
    }

def compile_c(path, cinput):
    """
    compile and execute C code
    """
    uuid = path.stem
    exec_path = EXEC_DIR / f'{uuid}'
    if os.name == 'nt':
        exec_path = exec_path.with_suffix('.exe')
    
    compile_process = subprocess.run(
        ['gcc', str(path), '-o', str(exec_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if compile_process.returncode != 0:
        return {
            'coutput': '',
            'cerror' : compile_process.stderr
        }
    
    run_process = subprocess.run(
        [str(exec_path)],
        input=cinput,
        capture_output=True,
    )
    return {
        'coutput': run_process.stdout,
        'cerr': run_process.stderr
    }

def compile_cpp(path, cinput):
    """
    compile and execute C++ code
    """
    uuid = path.stem
    exec_path = EXEC_DIR / f'{uuid}'
    if os.name == 'nt':
        exec_path = exec_path.with_suffix('.exe')
    
    compile_process = subprocess.run(
        ['g++', str(path), '-o', str(exec_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if compile_process.returncode != 0:
        return {
            'coutput': '',
            'cerror' : compile_process.stderr
        }
    
    run_process = subprocess.run(
        [str(exec_path)],
        input=cinput,
        capture_output=True,
    )
    return {
        'coutput': run_process.stdout,
        'cerr': run_process.stderr
    }

LANGAUGE_DISPATCH = {
    'py' : compile_python,
    'cpp' : compile_cpp,
    'c' : compile_c,
}

def execute(language, code, cinput) :
    """
     write the code to a file,
     call compile function
     return dict(coutput, cerror) 
    """

    uuid = uuid.uuid4()
    path = None
    if language in ['C++', 'C']:
        path = CODE_DIR / f'{uuid}.{language}'
    else: 
        path = EXEC_DIR / f'{uuid}.py'

    if path is None:
        return {
            'coutput': '',
            'cerr': 'Unsupported language'
        }
    
    with open(path, 'w') as f:
        f.write(code)

    return LANGAUGE_DISPATCH[language](path, cinput)
