'''
Main program
'''

import sys
from flask import Flask
from flask_restful import Resource, Api


if __name__ == "__main__":
    assert sys.version >= 3.5

    app = Flask(__name__)
    api = Api(app)

    class HomeResource(Resource):
        def get(self):
            return { 'jouons à': 'la contrée' }

    api.add_resource(HomeResource, '/')

    if __name__ == '__main__':

        app.run(host='0.0.0.0', debug=True)
