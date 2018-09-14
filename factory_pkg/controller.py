from factory_pkg import link
from factory_pkg import relations
from factory_pkg import common
from factory_pkg.cnc import axis
import logging

logger = logging.getLogger(__name__)


###################################################
# Controller_latest

class Controller_latest:
    def __init__(self, path):
        logger.debug('Controller_latest Init, path: %s', path)
        self.path = path
        self._manufacturer = ""
        self._controller_type = ""
        self._model = ""
        self._ip_address = ""

    def update(self):
        latest, valid = common.json_from_path([self.path])
        logger.debug('Controller_latest update, valid: %s', valid)
        if valid:
            self._manufacturer = latest["manufacturer"]
            self._controller_type = latest["controller_type"]
            self._model = latest["model"]
            self._ip_address = latest["ip_address"]
        
    def manufacturer(self):
        if not self._manufacturer:
            self.update()
        return self._manufacturer

    def controller_type(self):
        if not self._controller_type:
            self.update()
        return self._controller_type

    def model(self):
        if not self._model:
            self.update()
        return self._model

    def ip_address(self):
        if not self._ip_address:
            self.update()
        return self._ip_address


###################################################
# Controller

class Controller:
    def __init__(self, name, path = common.DEFAULT_API_SITE):
        logger.debug('Controller Init, name: %s', name)
        logger.debug('Controller Init, api_path: %s', path)
        
        common.DEFAULT_API_SITE = path

        self._link = link.Link( ["class", "controller", "instance", name])
        self.latest = Controller_latest(self._link.latest())
        self.relations = relations.Relations(self._link.relations())

