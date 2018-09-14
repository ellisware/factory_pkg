from urllib.parse import urlunsplit
import requests
import json
import logging

logger = logging.getLogger(__name__)


################################################
# Constants

DEFAULT_XA_SITE = "xa-site/v1"
DEFAULT_API_SITE = "api-rest:8083/field_api/v3"

################################################
# Reqeusts

def make_request(url):
    
    dictionary = {}
    valid = False
    
    try:
        logger.debug('make_request: %s', url)
        response = requests.get(url)
        response.raise_for_status()
        dictionary = json.loads(response.text)
        valid = True
    except requests.exceptions.Timeout:
        logger.exception('make_request: timeout')
    except requests.exceptions.HTTPError as e:
        logger.exception('make_request: http error: %s', e)
    except requests.exceptions.RequestException as e:
        logger.exception('make_request: exception: %s', e)
    except ValueError as e:
        logger.exception('make_request: json error')
    
    return dictionary, valid

def concat_paths(sequence):
    logger.debug('common.concat_paths: %s', sequence)
    result = []
    for path in sequence:
        result.append(path)
        if path.startswith('/'):
            break
    ret = '/'.join(result)
    logger.debug('common.concat_paths: %s', ret)
    return ret

def easy_url(path_parts, netlocation = DEFAULT_API_SITE):
    logger.debug('common.easy_url: %s', path_parts)
    scheme = 'http'
    netloc = netlocation
    hpath = concat_paths(path_parts)
    query = ''
    fragment = ''
    ret = urlunsplit((scheme, netloc , hpath , query, fragment))
    logger.debug('common.easy_url: %s', ret)
    return ret

def json_from_path(path):
    logger.debug('common.json_from_path: %s', path)
    response, valid = make_request(easy_url(path))
    logger.debug('common.json_from_path: valid=%s', valid)
    return response, valid



################################################
# Moments

def moments_parser(data, label):
    ret = {}
    for moment in data:
        ret[moment["unixtime"]] = moment["moment"][label]
    return ret
