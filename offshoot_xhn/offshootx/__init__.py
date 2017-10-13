from offshootx.base import *
from offshootx.manifest import Manifest
from offshootx.pluggable import Pluggable
config = load_configuration("offshoot.yml")
pluggable_classes = lambda: map_pluggable_classes()