import offshootx
import sys
import inspect
import ast
import offshoot
'''This is a dict which the keys are module names while the values are objects
  of modules'''
print(sys.modules.keys())
print(sys.modules['offshootx'])
print('Here we will check the inspect.getmembers')
print(inspect.getmembers(sys.modules['offshootx'],inspect.isclass))
print('\n')

class deco():
    def __init__(self):
        self._cat = 'mimi'
    @property
    def cat(self):
        return self._cat
    @classmethod
    def test_fn(cls):
        print(inspect.getsource(cls))
    @classmethod
    def find_deco(cls):
        result = dict()
        def visit_FunctionDef(node):
            result[node.name] = [ast.dump(e) for e in node.decorator_list]

        v = ast.NodeVisitor()
        v.visit_FunctionDef = visit_FunctionDef
        v.visit(compile(inspect.getsource(cls),'?','exec',ast.PyCF_ONLY_AST))

        return result
    @classmethod
    def filter(cls):
        result = cls.find_deco()
        for method_name,stru in result.items():
            stru_str = ''.join(stru)
            print(stru_str)
            if "id='property'" in stru_str:
                print(method_name)


    @classmethod
    def _find_decorators(cls):
        result = dict()

        def visit_FunctionDef(node):
            result[node.name] = [ast.dump(e) for e in node.decorator_list]

        v = ast.NodeVisitor()

        v.visit = visit_FunctionDef
        v.visit(compile(inspect.getsource(cls), '?', 'exec', ast.PyCF_ONLY_AST))

        return result
    @offshoot.accepted
    @classmethod
    def test_fn(self):
        pass






deco0 = deco()
#deco0.test_fn()
print('888888888')
print(deco0.find_deco())
print('99999999999')
print(deco0.filter())
