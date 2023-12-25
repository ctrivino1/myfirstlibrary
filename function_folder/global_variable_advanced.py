# global_variable_advanced.py
import pandas as pd

class GlobalVariables:
    def __init__(self):
        self.dataset1 = None
        self.column_name = None
        self.value1 = None
        self.advanced_variable = None

    def run_all_functions(self):
        global all_globals
        # Call all functions and update global variables
        self.function1()
        self.function2()
        self.function3()
        self.function4()
        print('finished')

    def function1(self):
        # Update global variables in function1
        global all_globals
        self.dataset1 = [1, 2, 3, 4, 5]

    def function2(self):
        # Update global variables in function2
        global all_globals
        self.column_name = 'example_column'

    def function3(self):
        # Update global variables in function3
        global all_globals
        self.value1 = 42

    def function4(self):
        # Update global variables in function4 (create a Pandas DataFrame)
        global all_globals
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        self.advanced_variable = pd.DataFrame(data)

