from urllib.parse import urlunsplit
import requests
import json


################################################
# Constants

# REST API Server
#IP = '192.168.82.57'
IP = '192.168.2.241'
PORT = '8083'
API = 'field_api/v3'

SITE = "http://192.168.2.241:40001/v1/node"


################################################
# Helpers

def concat_paths(sequence):
        result = []
        for path in sequence:
            result.append(path)
            if path.startswith('/'):
                break
        return '/'.join(result)

def easy_url(path_parts):
    scheme = 'http'
    netloc = IP + ':' + PORT + '/' + API
    hpath = concat_paths(path_parts)
    query = ''
    fragment = ''
    return urlunsplit((scheme, netloc , hpath , query, fragment))

def json_from_path(path):
    response = requests.get(easy_url(path))
    return json.loads(response.text)

def moments_parser(data, label):
    ret = {}
    for moment in data:
        ret[moment["unixtime"]] = moment["moment"][label]
    return ret