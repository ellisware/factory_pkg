from factory_pkg import link
from factory_pkg import common
###################################################
# Axis Class

class Axis:
    def __init__(self, instance_path):
        self._link = link.Link(instance_path)
        relations = common.json_from_path([self._link.relations])
        self._status = link.Link([relations["status_cnc_axis"][0]["link"]["instance"]])

        
        latest = common.json_from_path([self._link.latest])
        self.name = latest["axis_name"]
        self.type = latest["axis_type"]
        self.number = latest["axis_number"]
        self.path = latest["path_number"]
        self.path_axis_number = latest["path_axis_number"]
        
    def temperature(self):
        latest = common.json_from_path([self._status.latest])
        return latest["temperature"]
    
    def machine_position(self):
        latest = common.json_from_path([self._status.latest])
        return latest["machine_position"]
    
    def temperature_history(self, start, end, limit):
        url = self._status.moments + "?after=" + start + "&before=" + end + "&limit=" + limit + "&order=desc"
        moments_data = common.json_from_path([url])
        ret = common.moments_parser(moments_data, "temperature")
        return ret
        
    def moments_count(self, start, end):
        url = self._status.count + "?after=" + start + "&before=" + end
        count = common.json_from_path([url])
        return count["count"]
        