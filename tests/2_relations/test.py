import unittest
import httpretty
import logging
import sys
import json
import os
import requests

from factory_pkg import common
from factory_pkg import relations

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

##########################################
# Relations Testing

class RelationTests(unittest.TestCase):
   
    @httpretty.activate
    def test_relations(self):
        
        # Logging Decoration
        logger.debug("\n###################################")
        logger.debug("##########    RelationsTest    #########\n")


        # Load Mock REST API responses
        relations_response = os.path.join('', "controller.json")

        with open(relations_response) as f:
            relations_json = f.read()

        logger.debug("Relation content is registered as: %s \n", relations_json)

        # Register Mock http responses
        h_path = "/class/controller/instance/controller00001/relations"
        relations_url = "http://" + common.DEFAULT_API_SITE + h_path

        httpretty.register_uri(httpretty.GET, relations_url, body = relations_json, content_type = 'application/json')
        
        logger.debug("Relations url is registered as: %s \n", relations_url)

        # Test the response of the mock site
        response = requests.get(relations_url)
        logger.debug("The GET request returned code %s \n", response)
        assert relations_json == response.text

        # Test the links are populated correctly
        _relations = relations.Relations([h_path])
        _dict = _relations.relations()

        assert _dict["status"][0]["id"] == "status00007"
        assert _dict["status"][0]["link"]["instance"] == "/class/status/instance/status00007"

if __name__ == '__main__': 
    unittest.main()