import logging
import random

from flask import Response, json, jsonify


def get_random_from_collection(collection, item_key=None):
    """
    Returns a random item from a collection
    :param collection: Collection being searched
    :param item_key: A specific value that needs to be returned from the collection
    :return: A random item from a collection
    """
    try:
        index = random.randint(0, len(collection) - 1)
        if item_key is None:
            return collection[index]
        else:
            return collection[index][item_key]
    except Exception as e:
        logging.error(e.message)
        return None


def create_json_response(source):
    """
    Creates a response represented in json from a given source
    :param source: Object to represent as json
    :return: Response: Flask Response object
    """
    try:
        if source is None:
            return create_json_error_response(-2, "Response is empty!", 200)
        return Response(json.dumps(source.__dict__), status=200, mimetype='application/json')
    except Exception as e:
        logging.error('Error creating json response from %s,', source, e.message)


def create_json_error_response(code, description, http_status):
    """
    Creates an error response represented in json
    :param code: Error code
    :param description: Error description
    :param http_status: Http status of the response
    :return:
    """
    try:
        response = jsonify(status=code, description=description)
        response.status_code = http_status
        return response
    except Exception as e:
        logging.error('Error creating json error response from %s,', e.message)
