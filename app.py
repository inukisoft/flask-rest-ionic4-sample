from flask import Flask
from flask import json
from flask import Response
from flask_cors import CORS, cross_origin
import urllib.request

app = Flask(__name__)

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


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/v1/products")
@cross_origin()
def get_products():

	js = json.dumps(products)
	resp = Response(js, status=200, mimetype='application/json')
	return resp

@app.route("/api/v1/products/<id_p>")
@cross_origin()
def get_product(id_p):

    print ("id_p :" , id_p)
    js = json.dumps("[]")
    for i in products: 
        print ("elemento : " , i)
        print ("elemento i['_id']", i['_id'])
        if int(i['_id']) == int(id_p):
            js = json.dumps(i)
            print ("elemento encontrado _id =",id_p)

    print ("get element product :", js)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7776, debug=True)