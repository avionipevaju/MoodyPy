from flask import Flask

from moody_py.engine.engine import Engine

routing = Flask(__name__)
engine = Engine()


@routing.route("/")
def hello():
    return 'Hello Camel-Python Connection!'


@routing.route("/execute")
def execute():
    response = engine.execute_task()
    return response
