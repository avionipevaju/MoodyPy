from flask import Flask

import moody_py.utils as utils
from moody_py.engine.engine import Engine

routing = Flask(__name__)
engine = Engine()


@routing.route("/moody/api/execute")
def execute():
    """
    Rest endpoint for executing moody_py task with RESOLVE_WEATHER_DATA instruction
    :return: Response: Json represented TwitterResponse object
    """
    result = engine.execute_task()
    return utils.create_json_response(result)
