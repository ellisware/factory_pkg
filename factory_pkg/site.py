import requests
import json
from factory_pkg import common

##################################################
# Node Class

class Node:
    def __init__(self, site):
        self.id = site["id"]
        self.name = site["name"]
        self.controller_id = site["controller_id"]
        self.level = site["level"]
        self.position = site["position"]
        self.parent_id = site["parent_id"]
        self.child_id = site["child_id"]
        self.tag_id = site["tag_id"]
        
    def is_type(self):
        ret = ""
        if isinstance(self.controller_id, str) and len(self.controller_id) > 0 :
            data = common.json_from_path(["class","controller","instance",self.controller_id,"relations"])
            ret = list(data)[0]
        return ret
        

##################################################
# Site Class

class Site:
    def __init__(self):
        self.nodes = []
        response = requests.get(common.SITE)
        jresp = json.loads(response.text)
        for node in jresp:
            temp_node = Node(node)
            self.nodes.append(temp_node)
