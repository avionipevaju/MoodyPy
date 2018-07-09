import logging
import json

logging.basicConfig(format='%(asctime)s %(message)s', filename='logs.log', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)

try:
    with open('credentials.json') as json_file:
        credentials = json.load(json_file)
except IOError as e:
    logging.error('Error loading credentials file: %s', e.message)