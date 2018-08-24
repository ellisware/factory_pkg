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
DEFAULT_XA_SITE = "http://xa-site/v1"


################################################
# Reqeusts

def make_request(url):
    
    dictionary = {}
    valid = False
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dictionary = json.loads(response.text)
        valid = True
    except requests.exceptions.Timeout:
        # timeout
        placeholder = 1
    except requests.exceptions.RequestException as e:
        # failure
        placeholder = 1
    except requests.exceptions.HTTPError as e:
        # Response Failure 401 etc.
        placeholder = 1
    except ValueError as e:
        # Invalid JSON
        placeholder = 1
    
    return dictionary, valid

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
    response, valid = make_request(easy_url(path))
    return response, valid



################################################
# Moments

def moments_parser(data, label):
    ret = {}
    for moment in data:
        ret[moment["unixtime"]] = moment["moment"][label]
    return ret
