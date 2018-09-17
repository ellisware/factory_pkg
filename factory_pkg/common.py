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

def make_request(url) -> dict:
    """
    The make_request is an abstraction of requests.get and json.loads that catches asserts for graceful fail in the web app.

    Parameters
    ----------
    url : str
        the url to retrieve
    
    Output
    ----------
    response : dict
        A dictionary or nested dictionary from the json response.

    """
    
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


def concat_paths(sequence) -> str:
    """
    Corrects paths/concatenates paths with slashes to make proper url paths.

    Parameters
    ----------
    sequence : list
        a list of sections to concatenate to a url path
    
    Output
    ----------
    response : str
        The fully concatenated url path

    """

    logger.debug('common.concat_paths: %s', sequence)
    result = []
    for path in sequence:
        result.append(path)
        if path.startswith('/'):
            break
    ret = '/'.join(result)
    logger.debug('common.concat_paths: %s', ret)
    return ret


def easy_url(path_parts, netlocation = DEFAULT_API_SITE) -> str:
    """
    An abstraction of urlunsplit to eaily construct complete urls given the rest api pattern

    Parameters
    ----------
    path_parts : list
        a list of sections to concatenate to a url path
    netlocation : str
        the domain location of the rest-api
    
    Output
    ----------
    response : str
        The fully constructed url

    """

    logger.debug('common.easy_url: %s', path_parts)
    scheme = 'http'
    netloc = netlocation
    hpath = concat_paths(path_parts)
    query = ''
    fragment = ''
    ret = urlunsplit((scheme, netloc , hpath , query, fragment))
    logger.debug('common.easy_url: %s', ret)
    return ret

def json_from_path(path) -> dict:
    """
    An wrapper for make_request and easy_url

    Parameters
    ----------
    path : str
        a list of sections to concatenate to a url path
    
    Output
    ----------
    response : str
        The dictionary response from the api request

    """

    logger.debug('common.json_from_path: %s', path)
    response, valid = make_request(easy_url(path))
    logger.debug('common.json_from_path: valid=%s', valid)
    return response, valid



################################################
# Moments

def moments_parser(data, label) -> dict:
    """
    moments are returned from the rest api as a dictionary.  The moments parser returns a dictionary that only contains the specified label

    Parameters
    ----------
    data : dict
        The complete dictionary
    label : str
        The key value of moments to parse from the dictionary
    
    Output
    ----------
    response : dict
        A dictionary containing only the moments with the key matching the specified label

    """

    ret = {}
    for moment in data:
        ret[moment["unixtime"]] = moment["moment"][label]
    return ret
