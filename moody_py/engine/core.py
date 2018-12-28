from moody_py.engine.routing import routing

PORT = 8887
HOST = '0.0.0.0'

if __name__ == '__main__':
    routing.run(host=HOST, port=PORT)
