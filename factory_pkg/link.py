from factory_pkg import common

###################################################
# Link Class

class Link:
    def __init__(self, instance_path):
        instance = common.json_from_path(instance_path)
        self.instance = instance["link"]["instance"]
        self.latest = instance["link"]["latest"]
        self.history = instance["link"]["history"]
        self.moments = instance["link"]["moments"]
        self.relations = instance["link"]["relations"]
        self.count = instance["link"]["count"]