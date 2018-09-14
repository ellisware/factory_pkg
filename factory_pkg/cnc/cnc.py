from factory_pkg import link
from factory_pkg import common
from factory_pkg.cnc import axis
from factory_pkg import relations
import logging


logger = logging.getLogger(__name__)

###################################################
# CNC Class

class CNC:
    """
     A class used to represent a cnc

    ...

    Attributes
    ----------
    _path : str
        the original cnc_axis_path path provided at init
    _link : Link
        the link dictionary for this class
    _axis : List
        a list of Axis class instances representing each axis

    Methods
    -------
    update()
        calls the rest api to update the stored attributes
    axis(n)
        returns the nth instance of Axis from the list
    """

    def __init__(self, cnc_path):
        """
        Parameters
        ----------
        cnc_path : str
            the url to the cnc class(rest api class)
        """
        self._path = cnc_path
        self._axis = []
        self._link = link.Link(self._path)
        self._relatives = relations.Relations([self._link.relations()])
        

    def update(self):
        """Calls the rest api and updates the instance attributes"""
        
        # iterate through all axis to build a list of Axis instances in order
        logger.debug("Updating attributes of cnc instance")
        for axs in self._relatives.relations()["controller_cnc_axis"]:
            temp_axis = axis.Axis([axs["link"]["instance"]])
            index = 0
            for ax in self._axis:
                if (ax.number() < temp_axis.number()):
                    index += 1
            self._axis.insert(index, temp_axis)

    
    def axis(self, n =0) -> axis.Axis:
        """ return an instance of Axis class, update() if not present"""

        if not self._axis:
            self.update()
        
        return self._axis[n]