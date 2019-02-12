from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import reqparse, abort, Api, Resource
from resource import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

## Setup the API resource routing

api.add_resource(ProdListResource, '/api/v1/products/', endpoint='products')
api.add_resource(ProdResource, '/api/v1/products/<string:id>', endpoint='product')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7775, debug=True)