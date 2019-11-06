import os.path
import subprocess
import sys


def test_program():
    completed_process = run_program(b"Rodolfo\n42\n")
    got = {
        "returncode": completed_process.returncode,
        "stdout": completed_process.stdout,
        "stderr": completed_process.stderr,
    }
    want = {
        "returncode": 0,
        "stdout": b"What is your name: How old are you: Rodolfo will be 100 years old in the year 2072\n",
        "stderr": b"",
    }
    assert got == want


def run_program(input):
    return subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), "program.py")],
        input=input,
        capture_output=True,
    )
