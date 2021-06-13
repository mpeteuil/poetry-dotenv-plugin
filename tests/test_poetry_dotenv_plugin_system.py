import pytest

import os
import subprocess

@pytest.mark.system
def test_end_to_end_plugin_functionality():
    env_absolute_path = os.environ.get('GITHUB_WORKSPACE', os.getcwd())
    dotenv_file_path = os.path.join(env_absolute_path, '.env')

    with open(dotenv_file_path, 'w') as f:
        f.write("export MY_ENV_VAR='Hello World'\n")

    try:
        command = 'poetry run python -c "import os; print(os.environ[\'MY_ENV_VAR\'])"'
        output = subprocess.check_output(command, shell=True)

        assert output.decode('utf-8') == 'Hello World\n'
    finally:
        os.remove(dotenv_file_path)
