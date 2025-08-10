import os
from pathlib import Path
import subprocess
from django.conf import settings
import uuid

# define path to tmp directory


COMPILER_DIR = Path(settings.BASE_DIR) / 'compiler' / 'tmp'
CODE_DIR = COMPILER_DIR / 'code'
EXEC_DIR = COMPILER_DIR / 'executables'

def compile_python(path, cinput):
    """
    execute python code
    """
    process = subprocess.run(
        ['python', str(path)],
        input=cinput.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        'coutput': process.stdout.decode('utf-8', errors='replace'),
        'cerr': process.stderr.decode('utf-8', errors='replace')
    }

def compile_c(path, cinput):
    """
    compile and execute C code
    """
    uuid_name = path.stem
    exec_path = EXEC_DIR / f'{uuid_name}'
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
            'cerror' : compile_process.stderr.decode('utf-8', errors='replace')
        }
    
    run_process = subprocess.run(
        [str(exec_path)],
        input=cinput.encode(),
        capture_output=True,
    )
    return {
        'coutput': run_process.stdout.decode('utf-8', errors='replace'),
        'cerr': run_process.stderr.decode('utf-8', errors='replace')
    }

def compile_cpp(path, cinput):
    """
    compile and execute C++ code
    """
    uuid_name = path.stem
    exec_path = EXEC_DIR / f'{uuid_name}'
    
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
            'cerror' : compile_process.stderr.decode('utf-8', errors='replace')
        }
    
    run_process = subprocess.run(
        [str(exec_path)],
        input=cinput.encode(),
        capture_output=True,
    )
    return {
        'coutput': run_process.stdout.decode('utf-8', errors='replace'),
        'cerr': run_process.stderr.decode('utf-8', errors='replace')
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

    uuid_name = uuid.uuid4()

    CODE_DIR.mkdir(parents=True, exist_ok=True)
    EXEC_DIR.mkdir(parents=True, exist_ok=True)

    path = None
    if language in ['cpp', 'c']:
        path = CODE_DIR / f'{uuid_name}.{language}'
    else: 
        path = EXEC_DIR / f'{uuid_name}.py'

    if path is None:
        return {
            'coutput': '',
            'cerr': 'Unsupported language'
        }

    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)

    return LANGAUGE_DISPATCH[language](path, cinput)
