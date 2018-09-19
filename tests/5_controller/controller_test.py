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
from factory_pkg import relations
from factory_pkg.cnc import axis
from factory_pkg.cnc import cnc

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

##########################################
# Controller Testing

class ControllerTest(unittest.TestCase):
   
    @httpretty.activate
    def test_controller(self):
        
        # Logging Decoration
        logger.debug("\n###################################")
        logger.debug("##########    ControllerTest    #########\n")


        # Load Mock REST API responses
        relative_directory = ""
        control_cnc_axis_response = os.path.join(relative_directory, "cnc_axis.json")
        cnc_axis_relations_response = os.path.join(relative_directory, "axis_relations.json")
        status_cnc_axis_response = os.path.join(relative_directory, "status_cnc_axis.json")
        axis_status_latest_response = os.path.join(relative_directory, "axis_status_latest.json")
        control_cnc_response = os.path.join(relative_directory, "controller_cnc.json")
        control_cnc_relations_response = os.path.join(relative_directory, "controller_cnc_relations.json")
        controller_response = os.path.join(relative_directory, "controller.json")
        controller_latest_response = os.path.join(relative_directory, "controller_latest.json")


        with open(control_cnc_axis_response) as f:
            control_cnc_axis_json = f.read()
        with open(cnc_axis_relations_response) as f:
            cnc_axis_relations_json = f.read()
        with open(status_cnc_axis_response) as f:
            status_cnc_axis_json = f.read()
        with open(axis_status_latest_response) as f:
            axis_status_latest_json = f.read()
        with open(control_cnc_response) as f:
            control_cnc_json = f.read()
        with open(control_cnc_relations_response) as f:
            control_cnc_relations_json = f.read()
        with open(controller_response) as f:
            controller_json = f.read()
        with open(controller_latest_response) as f:
            controller_latest_json = f.read()

        logger.debug(" content is registered as: %s \n", control_cnc_axis_json)
        logger.debug(" content is registered as: %s \n", cnc_axis_relations_json)
        logger.debug(" content is registered as: %s \n", status_cnc_axis_json)
        logger.debug(" content is registered as: %s \n", axis_status_latest_json)
        logger.debug(" content is registered as: %s \n", control_cnc_json)
        logger.debug(" content is registered as: %s \n", control_cnc_relations_json)
        logger.debug(" content is registered as: %s \n", controller_json)
        logger.debug(" content is registered as: %s \n", controller_latest_json)

        # Register Mock http responses
        control_cnc_axis_path = "/class/controller_cnc_axis/instance/controller_cnc_axis00001"
        control_cnc_axis_url = "http://" + common.DEFAULT_API_SITE + control_cnc_axis_path

        cnc_axis_relations_path = "/class/controller_cnc_axis/instance/controller_cnc_axis00001/relations"
        cnc_axis_relations_url = "http://" + common.DEFAULT_API_SITE + cnc_axis_relations_path

        status_cnc_axis_path = "/class/status_cnc_axis/instance/status_cnc_axis00001"
        status_cnc_axis_url = "http://" + common.DEFAULT_API_SITE + status_cnc_axis_path

        axis_status_latest_path = "/class/status_cnc_axis/instance/status_cnc_axis00001/latest"
        axis_status_latest_url = "http://" + common.DEFAULT_API_SITE + axis_status_latest_path

        control_cnc_path = "/class/controller_cnc/instance/controller_cnc00001"
        control_cnc_url = "http://" + common.DEFAULT_API_SITE + control_cnc_path

        control_cnc_reations_path = "/class/controller_cnc/instance/controller_cnc00001/relations"
        control_cnc_relations_url = "http://" + common.DEFAULT_API_SITE + control_cnc_reations_path

        controller_path = "/class/controller/instance/controller00001"
        controller_url = "http://" + common.DEFAULT_API_SITE + controller_path

        controller_latest_path = "/class/controller/instance/controller00001/latest"
        controller_latest_url = "http://" + common.DEFAULT_API_SITE + controller_latest_path

        httpretty.register_uri(httpretty.GET, control_cnc_axis_url, body = control_cnc_axis_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, cnc_axis_relations_url, body = cnc_axis_relations_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, status_cnc_axis_url, body = status_cnc_axis_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, axis_status_latest_url, body = axis_status_latest_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, control_cnc_url, body = control_cnc_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, control_cnc_relations_url, body = control_cnc_relations_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, controller_url, body = controller_json, content_type = 'application/json')
        httpretty.register_uri(httpretty.GET, controller_latest_url, body = controller_latest_json, content_type = 'application/json')
        
        logger.debug("Link url is registered as: %s \n", control_cnc_axis_url)
        logger.debug("Link url is registered as: %s \n", cnc_axis_relations_url)
        logger.debug("Link url is registered as: %s \n", status_cnc_axis_url)
        logger.debug("Link url is registered as: %s \n", axis_status_latest_url)
        logger.debug("Link url is registered as: %s \n", control_cnc_url)
        logger.debug("Link url is registered as: %s \n", control_cnc_relations_url)
        logger.debug("Link url is registered as: %s \n", controller_url)
        logger.debug("Link url is registered as: %s \n", controller_latest_url)

        # Test the response of the mock site
        response = requests.get(control_cnc_axis_url)
        logger.debug("The GET request returned code %s \n", response)
        assert control_cnc_axis_json == response.text

        response = requests.get(cnc_axis_relations_url)
        logger.debug("The GET request returned code %s \n", response)
        assert cnc_axis_relations_json == response.text

        response = requests.get(status_cnc_axis_url)
        logger.debug("The GET request returned code %s \n", response)
        assert status_cnc_axis_json == response.text

        response = requests.get(axis_status_latest_url)
        logger.debug("The GET request returned code %s \n", response)
        assert axis_status_latest_json == response.text

        response = requests.get(control_cnc_url)
        logger.debug("The GET request returned code %s \n", response)
        assert control_cnc_json == response.text

        response = requests.get(control_cnc_relations_url)
        logger.debug("The GET request returned code %s \n", response)
        assert control_cnc_relations_json == response.text

        response = requests.get(controller_url)
        logger.debug("The GET request returned code %s \n", response)
        assert controller_json == response.text

        response = requests.get(controller_latest_url)
        logger.debug("The GET request returned code %s \n", response)
        assert controller_latest_json == response.text

        # Test the links are populated correctly
        _controller = controller.Controller(["/class/controller/instance/controller00001"])
        assert _controller.latest().controller_type() == "cnc"


if __name__ == '__main__': 
    unittest.main()