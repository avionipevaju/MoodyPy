from moody_py.engine.routing import routing

PORT = 8887
HOST = '127.0.0.1'

if __name__ == '__main__':
    routing.run(host=HOST, port=PORT)
