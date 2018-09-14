from factory_pkg import common
from factory_pkg import link
import logging

logger = logging.getLogger(__name__)

class Relations:
    """
    A class used to store the relational urls of this class(rest api class)

    ...

    Attributes
    ----------
    _path : str
    the original path to the class passed at init
    _relations : str
    a dictionary of all of the relations for this class

    Methods
    -------
    update()
    calls the rest api to update the complete relation dictionary
    relations()
    returns the stored _relations dictionary, updating if necessary
    """

    def __init__(self, relations_path):
        """
        Parameters
        ----------
        relations_path : str
            the url to the class which contains the relations
        """

        logger.debug('relations from path: %s', relations_path)
        self._path = relations_path
        self._relations = {}
        
    def update(self):
        """Calls the rest api and updates the entire relations dictionary"""

        logger.debug('Updating relations')
        relations, valid = common.json_from_path(self._path)
        self._relations = relations


    def relations(self) -> dict:
        """Returns the entire relations dictionary, updating if necessary"""

        if not self._relations:
            self.update()
        return self._relations