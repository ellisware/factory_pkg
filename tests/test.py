import unittest
import httpretty
import logging
import sys
import json
import os
import requests

from factory_pkg import common
from factory_pkg import site
from factory_pkg import link
from factory_pkg import controller
from factory_pkg import relation

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

##########################################
# Site Testing

class SiteTest(unittest.TestCase):
   
    @httpretty.activate
    def test_site(self):
        
        # Logging Decoration
        logger.debug("\n###################################")
        logger.debug("##########    SiteTest    #########\n")

        # Load Mock REST API responses
        site_response = os.path.join('httpmock', "site", "node.json")
        tag_response = os.path.join('httpmock', "site", "tag.json")

        with open(site_response) as f:
            site_json = f.read()
        with open(tag_response) as f:
            tag_json = f.read()

        logger.debug("Site content is registered as: %s \n", site_json)
        logger.debug("Tag content is registered as: %s \n", tag_json)


        # Register Mock http responses
        site_url = "http://" + common.DEFAULT_XA_SITE + "/node"
        tag_url = "http://" + common.DEFAULT_XA_SITE + "/tag"

        httpretty.register_uri(httpretty.GET, site_url, body = site_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, tag_url, body= tag_json, content_type = 'application/json')
        
        logger.debug("Site url is registered as: %s \n", site_url)
        logger.debug("Tag url is registered as: %s \n", tag_url)

        
        # Test the response of the mock site
        response = requests.get(site_url)
        logger.debug("The GET request returned code %s \n", response)
        assert site_json == response.text

        # Test the site.py:Site() Class init
        response = site.Site()
        assert response.nodes[0].id == 1
        assert response.nodes[1].name == "Factory1"


##########################################
# Controller
   
class ControllerTest(unittest.TestCase):
    
    @httpretty.activate
    def test_site(self):
        
        
        # Logging Decoration
        logger.debug("\n###################################")
        logger.debug("#######    ControllerTest    ######\n")

        # Load Mock REST API responses
        
        links_response = os.path.join('httpmock', "api", "links", "controller.json")
        latest_response = os.path.join('httpmock', "api", "latest", "controller.json")
        relations_response = os.path.join('httpmock', "api", "relations", "controller.json")

        logger.debug("links_response %s: ", links_response)
        logger.debug("latest_response %s: ", latest_response)
        logger.debug("relations_response %s: ", relations_response)

        with open(links_response) as f:
            links_json = f.read()
        with open(latest_response) as f:
            latest_json = f.read()
        with open(relations_response) as f:
            relations_json = f.read()

        
        logger.debug("Links content is registered as: %s \n", links_json)
        logger.debug("Latest content is registered as: %s \n", latest_json)
        logger.debug("Relations content is registered as: %s \n", relations_json)

        # Register Mock http responses
        links_url = "http://" + common.DEFAULT_API_SITE + "/class/controller/instance/controller00001"
        latest_url = "http://" + common.DEFAULT_API_SITE + "/class/controller/instance/controller00001/latest"
        relations_url = "http://" + common.DEFAULT_API_SITE + "/class/controller/instance/controller00001/relations"

        httpretty.register_uri(httpretty.GET, links_url, body = links_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, latest_url, body = latest_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, relations_url, body = relations_json, content_type = 'application/json')

        logger.debug("Links url is registered as: %s \n", links_url)
        logger.debug("Latest url is registered as: %s \n", latest_url)
        logger.debug("Relations url is registered as: %s \n", relations_url)

        # Test the response of the mock site
        response = requests.get(links_url)
        logger.debug("The GET request returned code %s \n", response)
        assert links_json == response.text

        response = requests.get(latest_url)
        logger.debug("The GET request returned code %s \n", response)
        assert latest_json == response.text

        response = requests.get(relations_url)
        logger.debug("The GET request returned code %s \n", response)

        assert relations_json == response.text

        # Test the site.py:Site() Class init
        response = controller.Controller("controller00001")
        assert response.latest.manufacturer() == "FANUC"

        response.relations.update()
        logger.debug("response.relations: %s" , response.relations.relations()["status_cnc"])

        logger.debug(response.axis(1))
        
        

if __name__ == '__main__': 
    unittest.main()