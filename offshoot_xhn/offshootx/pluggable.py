'''This is the pluggable class which can be inherited by other pluggable
class
this class has a main classmethod which is method_directives.
The method_directives classmethod will return a dict which gives
 out classmethods' names which were already divided into three groups.'''
import ast
import inspect
class Pluggable():
    def __init_(self,**kwargs):
        pass
    @classmethod
    def method_directives(cls):
        directives = {
            'accepted':cls._method_with_decorators('accepted'),
            'expected':cls._method_with_decorators('expected'),
            'forbidden':cls._method_with_decorator('forbidden')

        }
        return directives
    @classmethod
    def _method_with_decorator(cls,label):
        methods = []
        if not label in cls._allowed_labels():
            return methods
        methods_all = cls._find_decorators()
        for method_name,decorator_structure in methods_all.items():
            decorator_string = ''.join(decorator_structure)
            if f"attr='{label}'" in decorator_string:
                methods.append(method_name)

    @classmethod
    def _allowed_labels(cls):
        return ['accepted','expected','forbidden']
    @classmethod
    def _find_decorators(cls):
        v = ast.NodeVisitor()
        methods_all = dict()
        def visit_FunctionDef(Node):
            methods_all[Node.name] = [ast.dump(e) for e in Node.decorator_list]
        v.visit_FunctionDef = cls.visit_FunctionDef
        v.visit(compile(inspect.getsource(cls),'?','exec',ast.PyCF_ONLY_AST))
        return methods_all
    @classmethod
    def on_file_install(cls,**kwargs):
        #TODO
        pass
    @classmethod
    def on_file_uninstall(cls,**kwargs):
        print('CALLBACK: on_file_install',kwargs)
        #TODO
        pass







