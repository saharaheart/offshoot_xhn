'''This file aims to define the plugin class
Basic data resources in plugin class
libraries,plugins,files are all list
config is a dict
'''
import offshootx
import sys
import os
#Here need to pay attention

class PluginError(Exception):
    pass
class Plugin():
    '''Which contains name,version (both are are strings),
    libraries  ----a list of packages required for the plugin
    files  -----a list of file object target pluggable classes in the project
    plugins ----a list of plugin dependencies to check for before installing plugin
    config  ----a dict which can be self defined and in the original class(here)
    it will load the default configuration if no yaml file was provided'''
    name = 'Plugin'
    version = '0.0.0'
    libraries = []
    files = []
    plugins = []
    config = dict()

    @classmethod
    def install(cls):
        if offshootx.config['allow']['plugins'] is True:
            cls._verify_plugins_dependencies()
        if offshootx.config['allow']['files'] is True:
            cls._install_files()
    @classmethod
    def _verify_plugins_dependencies(cls):
        '''Compare needed with the ones already had'''
        manifest = offshootx.Manifest()
        missing_plugins = []
        for item in cls.plugins:
            if not manifest.contain_plugins(item):
                missing_plugins.append(item)
            if len(missing_plugins) ==0:
                print('plugins dependencies satisfied')
            else:
                print(f'The following plugins need to be installed before {missing_plugins}')
                raise PluginError('plugins dependencies need to be met')
    @classmethod
    def _install_files(cls):
        '''Install files contain following steps
        First   we need signals to indicate the install statement
        is_success ----- go through the whole process
        install_messages ---- gather the information from installing
        installed_files -----a list collect file_dict
        a pluggable_class ---- used to generate callback
        files(dict) offered by config provided by local plugin

         Second  is the pluggable validation
            it can be divided into two steps
            one is ----To check if pluggable file come from local plugin file
                       is in the one of pluggable files mentioned in config generated
                       by yml file.
                       pay attention that
                       There is a pluggable_classes which is a dict.
                       Is is used to store information provided by config from yml file
                       It is generated in base.py by map_pluggable_classes fn
                       It has following structure
                       the key is the name of pluggable model while the value is object
                       of the corresponding name
                       So we check the containing relationship
            The other is ------determine is_valid and generate messages
                               Here is an important function validate_plugin_file
                               which is also in base.py.It receives file_path,
                               pluggable name offered by local config,and directives.
                               It changes the is_valid and message lists
                               This function is used to check if forbidden methods were
                               used and manage the expected in directives

                       '''
        #Validate files
        is_success = True
        install_messages = []
        installed_files = []
        pluggable_classes = offshootx.pluggable_classes()
        is_valid = True

        for file_dict in cls.files:
            if 'pluggable' in file_dict:
                pluggable_path = f"{offshootx.config['file_paths']['plugins']}/{cls.name}/{file_dict['path']}"
                is_valid,messages = cls._validate_file(pluggable_path,file_dict['pluggable'])
                if is_valid == False:
                    is_success = False
                    continue
            installed_files.append(file_dict)
            #file callbacks
            if 'pluggable' in file_dict:




    @classmethod
    def _validate_file(cls,pluggable_path,file_dict_pluggable):
        pluggable_classes = offshootx.pluggable_classes()
        if not file_dict_pluggable in pluggable_classes:
            raise PluginError('#TODO')
        pluggable_class = pluggable_classes[file_dict_pluggable]
        '''Here is validate_plugin_file which is defined in base.py'''

        is_valid,messages = offshootx.validate_plugin_file(pluggable_path,file_dict_pluggable,pluggable_class.method_directives)
        return is_valid,messages









