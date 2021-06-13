import pytest

import re
import subprocess

@pytest.mark.integration
def test_end_to_end_integration():
    command = 'poetry run python -c "import os; print(os.environ[\'MY_ENV_VAR\'])"'
    output = subprocess.check_output(command, shell=True)

    assert output.decode('utf-8') == 'Hello World\n'
