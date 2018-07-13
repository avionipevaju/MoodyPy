import random
import logging


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
    except TypeError as e:
        logging.error(e.message)
