import ast
import inspect
import offshoot
from offshootx.pluggable import *
'''First is that it can parse a python file'''
tree = ast.parse('offshootx/shape.py')
#print(ast.dump(tree))
'''It can also parse a string'''
def basic_test():
    tree0 = ast.parse("print('Hello Word')")
    print(ast.dump(tree0))
    tree0_compile = compile(tree0, '', mode='exec')
    # it shows that compile will generate a code object
    print(tree0_compile)
    # exec can excute code object and string which has python code format
    exec(tree0_compile)
#basic_test()
'''ast.parse and compile should compare with each other
which means that they should use the corresponding mode'''
#TODO
'''Different Nodes'''

class test_for_nodes(Pluggable):

    list_a = [1,2,3,4]
    dict_a = {'red':"value"}
    a_constant = True
    a_operation = 1+3
    a = 3
    a_expression = a+1

    b = 'Hello world'
    #c will be a formatted value
    c = f'Here a is {a} while b is {b}'
    @offshoot.accepted
    @classmethod
    def dump_self(cls):
        #what inspect.getsource get is str
        source_code = inspect.getsource(cls)
        tree = ast.parse(source_code)
        print(ast.dump(tree))

test_code = test_for_nodes()
test_code.dump_self()
#print(ast.dump(ast.parse('1')))

