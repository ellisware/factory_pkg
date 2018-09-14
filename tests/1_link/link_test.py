import unittest
import httpretty
import logging
import sys
import json
import os
import requests

from factory_pkg import common
from factory_pkg import link

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

##########################################
# Link Testing

class LinkTest(unittest.TestCase):
   
    @httpretty.activate
    def test_link(self):
        
        # Logging Decoration
        logger.debug("\n###################################")
        logger.debug("##########    LinkTest    #########\n")


        # Load Mock REST API responses
        link_response = os.path.join('', "controller.json")

        with open(link_response) as f:
            link_json = f.read()

        logger.debug("Link content is registered as: %s \n", link_json)

        # Register Mock http responses
        h_path = "/class/controller/instance/controller00001"
        link_url = "http://" + common.DEFAULT_API_SITE + h_path

        httpretty.register_uri(httpretty.GET, link_url, body = link_json, content_type = 'application/json')
        
        logger.debug("Link url is registered as: %s \n", link_url)

        # Test the response of the mock site
        response = requests.get(link_url)
        logger.debug("The GET request returned code %s \n", response)
        assert link_json == response.text

        # Test the links are populated correctly
        _link = link.Link([h_path])

        assert _link.latest() == "/class/controller/instance/controller00001/latest"
        assert _link.history() == "/class/controller/instance/controller00001/history"
        assert _link.moments() == "/class/controller/instance/controller00001/moments"
        assert _link.relations() == "/class/controller/instance/controller00001/relations"
        assert _link.count() == "/class/controller/instance/controller00001/count"

if __name__ == '__main__': 
    unittest.main()