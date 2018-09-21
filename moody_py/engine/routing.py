from flask import Flask

import moody_py.utils as utils
from moody_py.engine.engine import Engine
from moody_py.models.models import Instruction

routing = Flask(__name__)
engine = Engine()


@routing.route('/moody/api/execute')
def execute():
    """
    Rest endpoint for executing moody_py task with RESOLVE_WEATHER_DATA instruction
    :return: Response: Json represented TwitterResponse object
    """
    result = engine.execute_task(instruction=Instruction.RESOLVE_WEATHER_DATA)
    return utils.create_json_response(result)


@routing.route('/moody/api/post/')
def post():
    """

    :return:
    """
    result = engine.execute_task(instruction=Instruction.RESOLVE_ARTIST, content='Mogwai')
    return utils.create_json_response(result)