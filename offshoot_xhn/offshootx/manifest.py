import json


class Manifest:
    def contain_plugins(self,plugin_name):
        with open(self.file_path,'r') as f:
            manifest = json.load(f.read())
            return plugin_name in manifest['plugins']



    #TODO
