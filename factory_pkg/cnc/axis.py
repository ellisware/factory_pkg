from factory_pkg import link
from factory_pkg import common
from factory_pkg import relations


###################################################
# Axis Class

class Axis:
    """
     A class used to represent a single cnc axis

    ...

    Attributes
    ----------
    _path : str
        the original cnc_axis_path path provided at init
    _link : Link
        the link dictionary for this class
    _status : Link
        the link dictionary for the status of this axis
    _name :  str
        the ascii name of the axis, such as X,Y,Z
    _type : str
        the type of the axis such as linear or rotary
    _number : str
        the ordinal number of the axis, such as 1,2,3
    _cnc_path : str
        the path the axis is assigned to
    _path_axis_number : str
        the ordinal number of this axis within the path


    Methods
    -------
    update()
        calls the rest api to update the stored attributes
    name()
        returns the stored axis name
    type()
        returns the stored axis type
    number()
        returns the stored axis number
    path()
        returns the stored axis path
    path_axis_number()
        returns the stored path_axis_number
    temperature()
        fetches the current motor temperature
    machine_position()
        fetches the current machine position for the axis
    temperature_history(start,end,limit)
        returns a dictionary of timestamp:temperature pairs for the specified period
    moments_count(start, end)
        returns a count of the number of records between the specified timestamps
    """

    def __init__(self, controller_cnc_axis_path):
        """
        Parameters
        ----------
        controller_cnc_axis_path : str
            the url to the cnc axis class(rest api class)
        """

        # Init all class attributes, actual values lazy loaded for effiecency
        self._path = controller_cnc_axis_path
        self._status = ""
        self._name = ""
        self._type = ""
        self._number = ""
        self._cnc_path = ""
        self._path_axis_number = ""
        self._link = link.Link(self._path)
        self._relatives = relations.Relations([self._link.relations()])
        self._status = link.Link([self._relatives.relations()["status_cnc_axis"][0]["link"]["instance"]])


    def update(self):
        """Calls the rest api and updates the instance attributes"""

        # Call the rest api and update all attributes
        latest = common.json_from_path([self._link.latest()])[0]
        self._name = latest["axis_name"]
        self._type = latest["axis_type"]
        self._number = latest["axis_number"]
        self._cnc_path = latest["path_number"]
        self._path_axis_number = latest["path_axis_number"]


    def name(self) -> str:
        """ return the name attribute, update() if not present"""

        if not self._name:
            self.update()
        return self._name


    def axtype(self) -> str:
        """ return the type attribute, update() if not present"""

        if not self._type:
            self.update()
        return self._type



    def number(self) -> str:
        """ return the number attribute, update() if not present"""

        if not self._number:
            self.update()
        return self._number


    def path(self) -> str:
        """ return the path attribute, update() if not present"""

        if not self._cnc_path:
            self.update()
        return self._cnc_path  


    def path_axis_number(self) -> str:
        """ return the path axis number attribute, update() if not present"""

        if not self._path_axis_number:
            self.update()
        return self._path_axis_number  
        

    def temperature(self) -> str:
        """ return the motor temperature after reading from the rest api """

        latest = common.json_from_path([self._status.latest()])[0]
        return latest["temperature"]
    

    def machine_position(self) -> str:
        """ return the machine position after reading from the rest api """

        latest = common.json_from_path([self._status.latest()])[0]
        return latest["machine_position"]
    

    def temperature_history(self, start, end, limit):
        """ return a dictionary of timestamp:temperatures
        
         Parameters
        ----------
        start : str
            unix timestamp(milliseconds) of the start time
        end : str
            unix timestamp(milliseconds) of the end time
        limit : str
            the maximum number of entries to return
        """

        # fetch the timestamp:temperature samples from the rest api
        url = self._status.moments + "?after=" + start + "&before=" + end + "&limit=" + limit + "&order=desc"
        moments_data = common.json_from_path([url])
        ret = common.moments_parser(moments_data, "temperature")
        return ret
        

    def moments_count(self, start, end) -> str:
        """ return the total count of moments for use in progress bars etc.
        
         Parameters
        ----------
        start : str
            unix timestamp(milliseconds) of the start time
        end : str
            unix timestamp(milliseconds) of the end time
        """

        # fetch the count of moments from the rest api
        url = self._status.count + "?after=" + start + "&before=" + end
        count = common.json_from_path([url])[0]
        return count["count"]
        