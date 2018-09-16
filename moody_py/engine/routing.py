import logging

from flask import Flask, json, Response, jsonify

from moody_py.engine.engine import Engine

routing = Flask(__name__)
engine = Engine()


@routing.route("/moody/api/execute")
def execute():
    result = engine.execute_task()
    return create_json_response(result)


def create_json_response(source):
    try:
        if source is None:
            return create_json_error_response(-2, "Response is empty!", 200)
        return Response(json.dumps(source.__dict__), status=200, mimetype='application/json')
    except Exception as e:
        logging.error(e.message)


def create_json_error_response(code, description, http_status):
    try:
        response = jsonify(status=code, description=description)
        response.status_code = http_status
        return response
    except Exception as e:
        logging.error(e.message)