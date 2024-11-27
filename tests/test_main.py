import pytest
from click.testing import CliRunner
from py_executable.main import file_processor
import os
import pandas as pd

# Path to the data directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT_DIR, "data")


def test_file_processor(tmp_path):

    # Paths for input and output files
    input_file = os.path.join(DATA_DIR, "input.csv")
    output_file = os.path.join(DATA_DIR, "output.csv")

    # Clean up any existing output file
    if os.path.exists(output_file):
        os.remove(output_file)

    runner = CliRunner()
    result = runner.invoke(file_processor, [input_file, output_file])

    # Debugging output if the test fails
    if result.exit_code != 0:
        print("Result output:", result.output)
        print("Exception:", result.exception)

    # Assertions
    df = pd.read_csv(output_file)
    assert 'processed' in df.columns, "processed column not found in output file"

