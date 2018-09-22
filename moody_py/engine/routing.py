from flask import Flask, request

import moody_py.utils as utils
from moody_py.engine.engine import Engine
from moody_py.models.models import ExecutionRequest

routing = Flask(__name__)
engine = Engine()


@routing.route('/moody/api/execute')
def execute():
    """
    Rest endpoint for executing moody_py basic functionality, resolving and posting Twitter content by weather data
    :return: Response: Json represented TwitterResponse object
    """
    result = engine.execute_task(ExecutionRequest())
    return utils.create_json_response(result)


@routing.route('/moody/api/post', methods=['POST'])
def post():
    """
    Rest endpoint for executing custom moody_py functionality.
    :return: Response: Json represented TwitterResponse object
    """
    execution_request = ExecutionRequest(request.get_json())
    result = engine.execute_task(execution_request)
    return utils.create_json_response(result)
