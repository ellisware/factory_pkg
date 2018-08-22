from factory_pkg import link
from factory_pkg import common
from factory_pkg.cnc import axis

###################################################
# CNC Class

class CNC:
    def __init__(self, instance_path):
        self._link = link.Link(instance_path)
        self.axis = []
        self.controller = []

        relations = common.json_from_path([self._link.relations])
        
        for axis in relations["controller_cnc_axis"]:
            temp_axis = axis.Axis([axis["link"]["instance"]])
            index = 0
            for axis in self.axis:
                if (axis.number < temp_axis.number):
                    index += 1
            self.axis.insert(index, temp_axis)