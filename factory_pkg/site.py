import requests
import json
import logging

logger = logging.getLogger(__name__)

from factory_pkg import common


##################################################
# Node Class

class Node:
    """
    A class used to repsent a node in the site information.  By Querying nodes, all of the attached equipment can be found.

    ...

    Attributes
    ----------
    _path : str
        the original path to the class passed at init
    _id : int
        the node id
    _name : str
        the name(label) of the node
    _controller_id : str
        The controller id is the top level class id.  All relations are attached to the controller_id
    _level : int
        the level(depth) of this node
    _position : int
        the position of the node within the level
    _parent_id : int
        the number of the parent node at that higher level
    _child_id : list
        a dict of children nodes to this node
    _tag_id : list


    Methods
    -------
    update()
        calls the rest api to update the stored attributes
    id() : int
        returns node id
    name() : str
        returns the name(label) of the node
    controller_id() : str
        Returns the controller id is the top level class id
    level() : int
        the level(depth) of this node
    position() : int
        the position of the node within the level
    parent_id() : int
        the number of the parent node at that higher level
    child_id() : list
        a dict of children nodes to this node
    tag_id() : list
    """

    def __init__(self, node_path):
        """
        Parameters
        ----------
        node_path : str
            the url to the individual node
        """

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
        """Calls the rest api and updates the instance attributes"""

        nodes_response, valid = common.make_request(self._path)
        self._id = nodes_response["id"]
        self._name = nodes_response["name"]
        self._controller_id = nodes_response["controller_id"]
        self._level = nodes_response["level"]
        self._position = nodes_response["position"]
        self._parent_id = nodes_response["parent_id"]
        self._child_id = nodes_response["child_id"]
        self._tag_id = nodes_response["tag_id"]
        
    def id(self) -> int:
        """ return the id attribute, update() if not present"""

        if not self._id:
            self.update()
        return self._id

    def name(self) -> str:
        """ return the name attribute, update() if not present"""

        if not self._name:
            self.update()
        return self._name

    def controller_id(self) -> int:
        """ return the controller_id attribute, update() if not present"""
        
        if not self._controller_id:
            self.update()
        return self._controller_id

    def level(self) -> int:
        """ return the level attribute, update() if not present"""

        if not self._level:
            self.update()
        return self._level

    def position(self) -> int:
        """ return the level attribute, update() if not present"""

        if not self._position:
            self.update()
        return self._position

    def parent_id(self) -> int:
        """ return the parent_id attribute, update() if not present"""

        if not self._parent_id:
            self.update()
        return self._parent_id

    def child_id(self) -> list:
        """ return the children attribute, update() if not present"""

        if not self._child_id:
            self.update()
        return self._child_id

    def tag_id(self) -> list:
        """ return the children attribute, update() if not present"""

        if not self._tag_id:
            self.update()
        return self._tag_id

    def is_type(self) -> str:
        """ return the current type of controller"""

        ret = ""
        if isinstance(self.controller_id(), str) and len(self.controller_id()) > 0 :
            data, valid = common.json_from_path(["class","controller","instance",self.controller_id(),"relations"])
            if len(data) > 0 and valid:
                ret = list(data)[0]
        return ret
        
##################################################
# Tag Type Class

class Tag_Type:
    STRING = 0
    IMAGE = 1
    ICON = 3


##################################################
# Tag Class

class Tag:
    """
    A class used to repsent the site tags.

    ...

    Attributes
    ----------
    _path : str
        TODO: needed
    _id : int
        TODO: needed
    _link_tag_id : int
        TODO: needed
    _own_app : str
        TODO: needed
    _position : int
        TODO: needed
    _root_id : int
        TODO: needed
    _tag_class_id : int
        TODO: needed
    _value : str
        TODO: needed


    Methods
    -------
    update()
        calls the rest api to update the stored attributes
    id() : int
        returns tag id
    link_tag_id() : int
        returns the link tag id of the node
    own_app() : str
        Returns the name of the application where tag will be registerd
    position() : int
        the position of this tag
    root_id() : int
        the root id of the tag
    tag_class_id() : int
        the tag class id
    value() : str
        a dict of children nodes to this node
    """

    def __init__(self, tag_path):
        """
        Parameters
        ----------
        tag_path : str
            the url to the tag
        """

        self._path = tag_path
        self._id = ""
        self._link_tag_id = ""
        self._own_app = ""
        self._position = ""
        self._root_id = ""
        self._tag_class_id = ""
        self._value = ""
        
    def update(self):
        """Calls the rest api and updates the instance attributes"""

        tags_response, valid = common.make_request(self._path)
        self._id = tags_response["id"]
        self._link_tag_id = tags_response["link_tag_id"]
        self._own_app = tags_response["own_app"]
        self._position = tags_response["position"]
        self._root_id = tags_response["root_id"]
        self._tag_class_id = tags_response["tag_class_id"]
        self._value = tags_response["value"]

    def id(self) -> int:
        """ return the id attribute, update() if not present"""

        if not self._id:
            self.update()
        return self._id

    def link_tag_id(self) -> int:
        """ return the link_tag_id attribute, update() if not present"""

        if not self._link_tag_id:
            self.update()
        return self._link_tag_id

    def own_app(self) -> str:
        """ return the own_app attribute, update() if not present"""

        if not self._own_app:
            self.update()
        return self._own_app

    def position(self) -> int:
        """ return the position attribute, update() if not present"""

        if not self._position:
            self.update()
        return self._position

    def root_id(self) -> int:
        """ return the root id attribute, update() if not present"""

        if not self._root_id:
            self.update()
        return self._root_id
        
    def tag_class_id(self) -> int:
        """ return the tag class id attribute, update() if not present"""

        if not self._tag_class_id:
            self.update()
        return self._tag_class_id

    def value(self) -> str:
        """ return the value attribute, update() if not present"""

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
                url = common.easy_url(["nodes", str(node["id"])], self._path)
                temp_node = Node(url)
                self._nodes.append(temp_node)

        tag_url = common.easy_url(["tag"], self._path)
        tag_dict, valid = common.make_request(tag_url)
        if valid:
            for tag in tag_dict:
                url = common.easy_url(["tag", str(tag["id"])], self._path)
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