import sys
import os
import pytest
import tempfile
from shutil import copyfile

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import budget_tracker

# Define a path for the temporary test data file
TEST_DATA_FILE = os.path.join(os.path.dirname(__file__), 'test_expenses.csv')

def setup_module(module):
    # Save the original data file path and create a temporary one for testing
    global original_data_file
    original_data_file = budget_tracker.DATA_FILE
    copyfile(original_data_file, TEST_DATA_FILE)
    budget_tracker.DATA_FILE = TEST_DATA_FILE

def teardown_module(module):
    # Restore the original data file path
    budget_tracker.DATA_FILE = original_data_file

def setup_function(function):
    # Clear the test data file before each test
    with open(TEST_DATA_FILE, 'w') as file:
        file.write('')

def test_add_expense():
    budget_tracker.add_expense('Groceries', 50)
    assert ['Groceries', '50'] in budget_tracker.view_expenses()
    assert budget_tracker.calculate_total() == 50

def test_remove_expense():
    budget_tracker.add_expense('Groceries', 50)
    budget_tracker.remove_expense('Groceries')
    assert ['Groceries', '50'] not in budget_tracker.view_expenses()
    assert budget_tracker.calculate_total() == 0

def test_multiple_expenses():
    budget_tracker.add_expense('Rent', 500)
    budget_tracker.add_expense('Utilities', 150)
    assert budget_tracker.calculate_total() == 650
    budget_tracker.remove_expense('Utilities')
    assert budget_tracker.calculate_total() == 500
