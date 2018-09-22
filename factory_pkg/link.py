from factory_pkg import common
import logging

logger = logging.getLogger(__name__)


###################################################
# Link Class

class Link:
    """
    A class used to store the urls of this specific class(rest api class)

    ...

    Attributes
    ----------
    _path : str
        the original path to the class passed at init
    _latest : str
        the url path for the latest class
    _history :  str
        the url path for the history class
    _moments : str
        the url path for the moments class
    _relations : str
        the url path for the relations class
    _count : str
        the url path for the count class


    Methods
    -------
    update()
        calls the rest api to update the stored attributes
    latest()
        returns the stored latest url
    history()
        returns the stored history url
    moments()
        returns the stored moments url
    relations()
        returns the stored relations url
    count()
        returns the stored count url
    """

    def __init__(self, link_path):
        """
        Parameters
        ----------
        link_path : str
            the url to the class of which to get links
        """

        logger.debug('link from path: %s', link_path)
        self._path = link_path
        self._latest = ""
        self._history = ""
        self._moments = ""
        self._relations = ""
        self._count = ""
        

    def update(self):
        """Calls the rest api and updates the instance attributes"""

        # Call the rest api and populate the attributes
        instance, valid = common.json_from_path(self._path)
        self._latest = instance["link"]["latest"]
        self._history = instance["link"]["history"]
        self._moments = instance["link"]["moments"]
        self._relations = instance["link"]["relations"]
        self._count = instance["link"]["count"]

    def latest(self) -> str:
        """ return the latest attribute, update() if not present"""

        if not self._latest:
            self.update()
        return self._latest


    def history(self) -> str:
        """ return the history attribute, update() if not present"""

        if not self._history:
            self.update()
        return self._history

    def moments(self) -> str:
        """ return the moments attribute, update() if not present"""

        if not self._moments:
            self.update()
        return self._moments


    def relations(self) -> str:
        """ return the relations attribute, update() if not present"""

        if not self._relations:
            self.update()
        return self._relations


    def count(self) -> str:
        """ return the count attribute, update() if not present"""

        if not self._count:
            self.update()
        return self._count


