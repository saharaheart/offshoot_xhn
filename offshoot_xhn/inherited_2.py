import os
def load_config():
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
config = load_config()