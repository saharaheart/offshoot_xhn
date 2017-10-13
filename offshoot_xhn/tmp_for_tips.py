'''Here will show the how to parse a python file
pay attention to using the dump fn in ast which help to visualize the object'''

import ast
import sys
import os
file_path = os.path.join(os.path.dirname(__file__),'rectangle.py')
print(file_path)
print(ast.ClassDef)

with open(file_path,'r') as f:

    syntax_tree = ast.parse(f.read())
    print(ast.dump(syntax_tree))
    print(syntax_tree.body)
    for statement in ast.walk(syntax_tree):
        if isinstance(statement,ast.ClassDef):
            print(ast.dump(statement))




