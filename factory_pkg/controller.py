from factory_pkg import link
from factory_pkg import relations
from factory_pkg import common
from factory_pkg.cnc import axis
import logging

logger = logging.getLogger(__name__)


###################################################
# Controller_latest

class Controller_latest:
    """
    A class used to represent a controllers 'latest' info from the rest-api

    ...

    Attributes
    ----------
    _path : str
    the original cnc_axis_path path provided at init
    _link : Link
    the link dictionary for this class
    _manufacturer : str
    The manufacturer returned from the rest api
    _controller_type : str
    The controller type returned from the rest api
    _model : str
    The model returned from the rest api
    _ip_address : str
    The ip address returned from the rest api

    Methods
    -------
    update()
    calls the rest api to update the stored attributes
    manufacturer()
    returns the manufacturer, updates if not retrieved yet
    controller_type()
    returns the controller type, updates if not retrieved yet
    model()
    returns the model, updates if not retrieved yet
    ip_address()
    returns the ip address, updates if not retrieved yet    
    """

    def __init__(self, latest_path):
        """
        Parameters
        ----------
        latest_path : str
            the url to the controller instance(rest api class)
        """

        logger.debug('Controller_latest Init, path: %s', latest_path)
        self._path = latest_path
        self._manufacturer = ""
        self._controller_type = ""
        self._model = ""
        self._ip_address = ""

    def update(self):
        """Calls the rest api and updates the instance attributes"""

        latest, valid = common.json_from_path([self._path])
        logger.debug('Controller_latest update, valid: %s', valid)
        if valid:
            self._manufacturer = latest["manufacturer"]
            self._controller_type = latest["controller_type"]
            self._model = latest["model"]
            self._ip_address = latest["ip_address"]

    def manufacturer(self):
        """ returns the manufacturer, update() if not present"""

        if not self._manufacturer:
            self.update()
        return self._manufacturer

    def controller_type(self):
        """ returns the controller_type, update() if not present"""

        if not self._controller_type:
            self.update()
        return self._controller_type

    def model(self):
        """ returns the model, update() if not present"""

        if not self._model:
            self.update()
        return self._model

    def ip_address(self):
        """ returns the ip address, update() if not present"""

        if not self._ip_address:
            self.update()
        return self._ip_address


###################################################
# Controller

class Controller:
    """
    A class used to represent a controller from the rest-api

    ...

    Attributes
    ----------
    _path : str
    the original cnc_axis_path path provided at init
    _link : Link
    the link dictionary for this class
    _manufacturer : str
    The manufacturer returned from the rest api
    _controller_type : str
    The controller type returned from the rest api
    _model : str
    The model returned from the rest api
    _ip_address : str
    The ip address returned from the rest api

    Methods
    -------
    update()
    calls the rest api to update the stored attributes
    manufacturer()
    returns the manufacturer, updates if not retrieved yet
    controller_type()
    returns the controller type, updates if not retrieved yet
    model()
    returns the model, updates if not retrieved yet
    ip_address()
    returns the ip address, updates if not retrieved yet    
    """

    def __init__(self, controller_path):
        """
        Parameters
        ----------
        _path : str
            the path to the controller instance(rest api class)
        """

        self._path = controller_path
        self._link = link.Link(self._path)
        self._latest = Controller_latest(self._link.latest())
        self._relations = relations.Relations(self._link.relations())


    def latest(self):
        """ return an instance of latest class, update() if not present"""

        return self._latest
