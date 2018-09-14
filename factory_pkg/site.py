import requests
import json
import logging

logger = logging.getLogger(__name__)

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
            data, valid = common.json_from_path(["class","controller","instance",self.controller_id,"relations"])
            if len(data) > 0 and valid:
                ret = list(data)[0]
        return ret
        
        
##################################################
# Tag Class

class Tag:
    def __init__(self, tag):
        self.id = tag["id"]
        self.link_tag_id = tag["link_tag_id"]
        self.own_app = tag["own_app"]
        self.position = tag["position"]
        self.root_id = tag["root_id"]
        self.tag_class_id = tag["tag_class_id"]
        self.value = tag["value"]
        
        
##################################################
# Site Class

class Site:
    def __init__(self, path = common.DEFAULT_XA_SITE):
        self.nodes = []
        self.tags = []

        node_url = common.easy_url(["node"], path)
        nodes_dict, valid = common.make_request(node_url)
        if valid:
            for node in nodes_dict:
                temp_node = Node(node)
                self.nodes.append(temp_node)
            
        tag_url = common.easy_url(["tag"], path)
        tag_dict, valid = common.make_request(tag_url)
        if valid:
            for tag in tag_dict:
                temp_tag = Tag(tag)
                self.tags.append(temp_tag)
