import requests
import json
import logging

logger = logging.getLogger(__name__)

from factory_pkg import common


##################################################
# Node Class

class Node:
    def __init__(self, node_path):
        self._path = node_path
        self._id = ""
        self._name = ""
        self._controller_id = ""
        self._level = ""
        self._position = ""
        self._parent_id = ""
        self._child_id = ""
        self._tag_id = ""

    def update(self):
        nodes_response, valid = common.make_request(self._path)
        self._id = nodes_response["id"]
        self._name = nodes_response["name"]
        self._controller_id = nodes_response["controller_id"]
        self._level = nodes_response["level"]
        self._position = nodes_response["position"]
        self._parent_id = nodes_response["parent_id"]
        self._child_id = nodes_response["child_id"]
        self._tag_id = nodes_response["tag_id"]
        
    def id(self):
        if not self._id:
            self.update()
        return self._id

    def name(self):
        if not self._name:
            self.update()
        return self._name

    def controller_id(self):
        if not self._controller_id:
            self.update()
        return self._controller_id

    def level(self):
        if not self._level:
            self.update()
        return self._level

    def position(self):
        if not self._position:
            self.update()
        return self._position

    def parent_id(self):
        if not self._parent_id:
            self.update()
        return self._parent_id

    def child_id(self):
        if not self._child_id:
            self.update()
        return self._child_id

    def tag_id(self):
        if not self._tag_id:
            self.update()
        return self._tag_id

    def is_type(self):
        ret = ""
        if isinstance(self.controller_id(), str) and len(self.controller_id()) > 0 :
            data, valid = common.json_from_path(["class","controller","instance",self.controller_id(),"relations"])
            if len(data) > 0 and valid:
                ret = list(data)[0]
        return ret
        
        
##################################################
# Tag Class

class Tag:
    def __init__(self, tag_path):
        self._path = tag_path
        self._id = ""
        self._link_tag_id = ""
        self._own_app = ""
        self._position = ""
        self._root_id = ""
        self._tag_class_id = ""
        self._value = ""
        
    def update(self):
        tags_response, valid = common.make_request(self._path)
        self._id = tags_response["id"]
        self._link_tag_id = tags_response["link_tag_id"]
        self._own_app = tags_response["own_app"]
        self._position = tags_response["position"]
        self._root_id = tags_response["root_id"]
        self._tag_class_id = tags_response["tag_class_id"]
        self._value = tags_response["value"]

    def id(self):
        if not self._id:
            self.update()
        return self._id

    def link_tag_id(self):
        if not self._link_tag_id:
            self.update()
        return self._link_tag_id

    def own_app(self):
        if not self._own_app:
            self.update()
        return self._own_app

    def position(self):
        if not self._position:
            self.update()
        return self._position

    def root_id(self):
        if not self._root_id:
            self.update()
        return self._root_id
        
    def tag_class_id(self):
        if not self._tag_class_id:
            self.update()
        return self._tag_class_id

    def value(self):
        if not self._value:
            self.update()
        return self._value
        
##################################################
# Site Class

class Site:
    def __init__(self, path = common.DEFAULT_XA_SITE):
        self._path = path
        self._nodes = []
        self._tags = []

    def update(self):
        node_url = common.easy_url(["node"], self._path)
        nodes_dict, valid = common.make_request(node_url)
        if valid:
            for node in nodes_dict:
                url = common.easy_url(["nodes", node["id"]], self._path)
                temp_node = Node(url)
                self._nodes.append(temp_node)

        tag_url = common.easy_url(["tag"], self._path)
        tag_dict, valid = common.make_request(tag_url)
        if valid:
            for tag in tag_dict:
                url = common.easy_url(["tag", tag["id"]], self._path)
                temp_tag = Tag(tag)
                self._tags.append(temp_tag)

    def nodes(self):
        if not self._nodes:
            self.update()
        return self._nodes

    def tags(self):
        if not self._tags:
            self.update()
        return self._tags