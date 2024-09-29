import os
import subprocess

# Added to exceute the Flask app from the root directory
base_dir = os.path.dirname(os.path.abspath(__file__))

os.environ['FLASK_APP'] = os.path.join(base_dir, 'src', 'backend', 'app.py')

os.environ['FLASK_ENV'] = 'development'

os.chdir(os.path.join(base_dir, 'src', 'backend'))

python_executable = os.path.join(base_dir, 'venv', 'Scripts', 'python.exe')

subprocess.run([python_executable, '-m', 'flask', 'run'], check=True)
