#lesson flaskresful

from flask import Flask #import flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()


class Quotes(Resource):
    def get(self):
        return {
            'silas':{
            'quote':['winners show up',
            'no retreat no surrender',
            'together we arw stronger']
            },
            'paul':{
            'quote':['I am the best.']
            }
    }

    def post(self):
        parser.add_argument('quote', type=str)
        args = parser.parse_args()

        return {
           'status': True,
           'quote': '{} added. Godd'.format(args['quote'])
    }

    def put(self, id):
        parser.add_argument('quotes', type=str)
        args = parser.parse_args()

        return {
            'id': id,
            'status': True,
            'quote': 'The quote numbered {} was updated.'.format(id)
    }

api.add_resource(Quotes, '/','/update/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, port=5004)
