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

api.add_resource(EquipoListResource, '/api/v1/equipos/', endpoint='equipos')
api.add_resource(AreaListResource, '/api/v1/areas/', endpoint='areas')


api.add_resource(CuasiListResource, '/api/v1/cuasis/', endpoint='cuasis')
api.add_resource(CuasiResource, '/api/v1/cuasis/', endpoint='cuasi')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7775, debug=True)