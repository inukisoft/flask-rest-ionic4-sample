from datetime import datetime
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

import sqlite3

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


equipos = [
  {
    '_id': '100',
    'equipo' : 'Llenadora'
  },
  {
    '_id': '101',
    'equipo' : 'Lavadora'
  },
    {
    '_id': '102',
    'equipo' : 'Etiquetadora'
  },
    {
    '_id': '103',
    'equipo' : 'Plaetizadora'
  },
    {
    '_id': '104',
    'equipo' : 'Despaletizadora'
  },
    {
    '_id': '105',
    'equipo' : 'Encajonadora'
  },
    {
    '_id': '106',
    'equipo' : 'Desencajonadora'
  },
    {
    '_id': '107',
    'equipo' : 'Empacadora'
  },
    {
    '_id': '108',
    'equipo' : 'Sala de preparación'
  },
    {
    '_id': '109',
    'equipo' : 'Pasteurizador'
  },
    {
    '_id': '110',
    'equipo' : 'Alexus'
  },
    {
    '_id': '111',
    'equipo' : 'Inspector de botellas'
  },
    {
    '_id': '112',
    'equipo' : 'Sopladora'
  },
    {
    '_id': '113',
    'equipo' : 'Sala de elaboración'
  },
    {
    '_id': '114',
    'equipo' : 'Sala Bag in Box'
  },
    {
    '_id': '115',
    'equipo' : 'Sala de calderas'
  },
    {
    '_id': '116',
    'equipo' : 'Sala de compresores'
  },
    {
    '_id': '117',
    'equipo' : 'Planta de agua'
  },
    {
    '_id': '118',
    'equipo' : 'Sala de osmosis'
  },
    {
    '_id': '119',
    'equipo' : 'Transito peatonal'
  },
    {
    '_id': '120',
    'equipo' : 'Vias de transporte'
  },
    {
    '_id': '121',
    'equipo' : 'Almacen de materias primas'
  },
    {
    '_id': '122',
    'equipo' : 'Almacen de repuestos'
  },
    {
    '_id': '123',
    'equipo' : 'Bodegas de productos químicos'
  }
];

areas = [
  { '_id': '1001', 'area' : 'Almacén' },
  { '_id': '1002', 'area' : 'Casino' },
  { '_id': '1003', 'area' : 'Elaboración' },
  { '_id': '1004', 'area' : 'Exteriores, Baños' },
  { '_id': '1005', 'area' : 'Linea 1' },
  { '_id': '1006', 'area' : 'Linea 2' },
  { '_id': '1007', 'area' : 'Linea 3' },
  { '_id': '1008', 'area' : 'Linea 4' },
  { '_id': '1009', 'area' : 'Linea 5' },
  { '_id': '1010', 'area' : 'Linea 6' },
  { '_id': '1011', 'area' : 'Linea 7' },
  { '_id': '1012', 'area' : 'Linea 8' },
  { '_id': '1013', 'area' : 'Linea 9' },
  { '_id': '1014', 'area' : 'Linea 10' },
  { '_id': '1015', 'area' : 'Linea 11' },
  { '_id': '1016', 'area' : 'Linea 12' },
  { '_id': '1017', 'area' : 'Linea 14' },
  { '_id': '1018', 'area' : 'Linea 15' },
  { '_id': '1019', 'area' : 'Taller de Mantenimiento' },
  { '_id': '1020', 'area' : 'Suministros' },
  { '_id': '1021', 'area' : 'Ecolab' },
  { '_id': '1022', 'area' : 'Viostec' },
  { '_id': '1023', 'area' : 'Resiter' }
];
 

equipo_fields = {
    '_id': fields.Integer,
    'equipo': fields.String
}

area_fields = {
    '_id': fields.Integer,
    'area': fields.String
}
      
prod_fields = {
    '_id': fields.Integer,
    'prod_name': fields.String,
    'prod_desc': fields.String,
    'prod_price': fields.String,
    'updated_at': fields.String
}

cuasi_fields = {
    'id' : fields.Integer,
    'rut' : fields.String,
    'area' : fields.Integer,
    'equipo': fields.Integer,
    'fechacuasi': fields.String,
    'describa': fields.String,
    'accion': fields.Integer,
    'informo': fields.Integer,
    'tipotrabajador': fields.String  
}

parser = reqparse.RequestParser()
parser.add_argument('prod_name')
parser.add_argument('prod_desc')
parser.add_argument('prod_price')
parser.add_argument('updated_at')

# parser para los nuevos cuasi accidentes y su almacenamiento en una bd
parser_cuasi = reqparse.RequestParser()
parser_cuasi.add_argument('rut')
parser_cuasi.add_argument('area')
parser_cuasi.add_argument('equipo')
parser_cuasi.add_argument('fechacuasi')
parser_cuasi.add_argument('describa')
parser_cuasi.add_argument('accion')
parser_cuasi.add_argument('informo')
parser_cuasi.add_argument('tipotrabajador')


class CuasiResource(Resource):

  @marshal_with(cuasi_fields)
  def post(self):

    print("en el post - add de un cuasi")
    
    parsed_args = parser_cuasi.parse_args()
    conn = sqlite3.connect('db/cuasiaccidente.db')
    c = conn.cursor()
    params = [parsed_args['rut'], parsed_args['area'], parsed_args['equipo'], parsed_args['fechacuasi'], parsed_args['describa'], parsed_args['accion'], parsed_args['informo'], parsed_args['tipotrabajador']]
    # a insertar los valores
    c.execute('insert into cuasi_accidentes (cuasi_rut, cuasi_area, cuasi_equipo, cuasi_fechacuasi, cuasi_describa, cuasi_accion, cuasi_informo, cuasi_tipotrabajador) values (?,?,?,?,?,?,?)', params) 
    # recuperemos el último valor ingresado 
    last_id = c.lastrowid
    print("last id: " , last_id)

    con.close()

    return {}, 201 

class CuasiListResource(Resource):

  @marshal_with(cuasi_fields)
  def get(self):

    conn = sqlite3.connect('db/cuasiaccidente.db')
    c = conn.cursor()
    c.execute('select * from cuasi_accidentes')
    rows = c.fetchall()
    salida = []

    for row in rows:
      fila = {'id': row[0], 'rut': row[1], 'area': row[2], 'equipo': row[3], 'fechacuasi':row[4], 'describa': row[5], 'accion': row[6], 'informo': row[7], 'tipotrabajador': row[8]}
      salida.append(fila)

    return salida, 200




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

class AreaListResource(Resource):

  @marshal_with(area_fields)
  def get(self):
    return areas, 200

class EquipoListResource(Resource):

  @marshal_with(equipo_fields)
  def get(self):
    return equipos, 200

