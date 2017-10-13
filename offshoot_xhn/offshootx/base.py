import sys
import inspect
import ast
import os
from offshootx.pluggable import Pluggable
def load_configuration(path = None):
    if path:
        #TODO
        pass
    else:
        return {
        "modules": [],
        "file_paths": {
            "plugins": "plugins",
            "config": "config/config.plugins.yml".replace("/", os.sep),
            "libraries": "requirements.plugins.txt"
        },
        "allow": {
            "files": True,
            "config": True,
            "plugins": True,
            "libraries": True,
            "callbacks": True
        },
        "sandbox_configuration_keys": True
    }
def map_pluggable_classes(config):
    '''It contains a pluggable classes.To get the object of the classes
     which were inherited from pluggable in module.
     inspect.getmenbers can get the specific pair (value,object)
     with specific type. And sys.modules can get the object of the module
    IF it is inherited from some classes can be judged from built-in fn
    issubclass()'''
    pluggable_classes = dict()
    module_lists = config['modules']
    for i in module_lists:
        exec(sys.modules[i])
        pair_list = inspect.getmembers(sys.modules[i],inspect.isclass)
        for j in pair_list:
            if issubclass(i[1],Pluggable):
                pluggable_classes[i[0]] = i[1]
    return pluggable_classes
def validate_plugin_file(file_path,pluggable_name,directives):
    '''It aims to check in pluggable class, if there is forbidden classmethod used and remove
    the expected classmethod
    It receives file_path,pluggable_name,directives
    it uses boolen seen_pluggable'''
    seen_pluggable = False
    is_valid = True
    messages = []
    with open('file_path','r') as f:
        tree = ast.parse(f.read())
        current_expected = directives['expected']
        for statement in ast.walk(tree):
            if isinstance(statement,ast.ClassDef):
                class_name = statement.name
                bases = list(map(lambda b:b.id if isinstance(b,ast.Name) else b.attr ,statement.bases))
                if pluggable_name in bases:
                    seen_pluggable = True
                    for item in statement.body:
                        if isinstance(item,ast.FunctionDef):
                            if item.name in directives['forbidden']:
                                is_valid = False
                                messages.append(f'{item.name} should not appear')
                            if item.name in current_expected:
                                current_expected.remove(item.name)
                    if len(current_expected):
                        is_valid = False
                        messages.append('There are still expected unsatisfied')
    if seen_pluggable == False:
        messages.append('unseen pluggable in bases')
    return is_valid,messages















