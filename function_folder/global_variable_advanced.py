# global_variable_advanced.py

class GlobalVariables:
    def __init__(self):
        self.dataset1 = None
        self.column_name = None
        self.value1 = None
        self.advanced_variable = None

def run_all_functions():
    global all_globals

    # Call all functions and update global variables
    function1()
    function2()
    function3()
    function4()

def function1():
    # Update global variables in function1
    global all_globals
    all_globals.dataset1 = [1, 2, 3, 4, 5]

def function2():
    # Update global variables in function2
    global all_globals
    all_globals.column_name = 'example_column'

def function3():
    # Update global variables in function3
    global all_globals
    all_globals.value1 = 42

def function4():
    # Update global variables in function4 (create a Pandas DataFrame)
    global all_globals
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    all_globals.advanced_variable = pd.DataFrame(data)

# Initialize the global variables object
all_globals = GlobalVariables()
