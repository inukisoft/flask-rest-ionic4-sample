from datetime import datetime
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with


products = [
    {
        '_id': 1,
        'prod_name':  'Buy groceries 1',
        'prod_desc':  'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'prod_price': 100,
        'updated_at': '2012-12-31 15:54:42.915204'
    },
    {
        '_id': 2,
        'prod_name':  'Buy groceries 2',
        'prod_desc':  'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'prod_price': 100,
        'updated_at': '2012-12-31 15:54:42.915204'
    },
    {
        '_id': 3,
        'prod_name':  'Buy groceries 3',
        'prod_desc':  'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'prod_price': 100,
        'updated_at': '2012-12-31 15:54:42.915204'
    },
    {
        '_id': 4,
        'prod_name':  'Buy groceries 4',
        'prod_desc':  'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'prod_price': 100,
        'updated_at': '2012-12-31 15:54:42.915204'
    },

];
      
prod_fields = {
    '_id': fields.Integer,
    'prod_name': fields.String,
    'prod_desc': fields.String,
    'prod_price': fields.String,
    'updated_at': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('prod_name')
parser.add_argument('prod_desc')
parser.add_argument('prod_price')
parser.add_argument('updated_at')


class ProdResource(Resource):

  @marshal_with(prod_fields)
  def get(self, id):
    for i in products: 
      print ("elemento : " , i)
      print ("elemento i['_id']", i['_id'])
      if int(i['_id']) == int(id):
        return i, 200
    return {}, 200

  def put(self, id):
    
    parsed_args = parser.parse_args()
    for i in products: 

      if int(i['_id']) == int(id):
        # editamos todo el elemento con lo nuevo que recibimos
        i['prod_name'] = parsed_args['prod_name']
        i['prod_desc'] = parsed_args['prod_desc']
        i['prod_price'] = parsed_args['prod_price']
        i['updated_at'] = parsed_args['updated_at'] 

        return i, 200
    
    return {}, 200

  def delete(self, id):
    return {}, 204

class ProdListResource(Resource):

  @marshal_with(prod_fields)
  def get(self):
    return products, 200

