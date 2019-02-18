from flask import Flask, request, jsonify
from flask import make_response
from flask_cors import CORS, cross_origin
from flask_restful import reqparse, abort, Api, Resource
from resource import *

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with


from io import StringIO
import io
from datetime import datetime

import sqlite3
import csv

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


app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "http://localhost:8100"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):

  print("en after_request :", response)	
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


# endpoint to create new cuasi
@app.route("/api/v1/cuasis", methods=["POST"])
def add_cuasi():
  print("en el post - add de un cuasi")
    
  conn = sqlite3.connect('db/cuasiaccidente.db')
  c = conn.cursor()
  params = [request.json['rut'], request.json['area'], request.json['equipo'], request.json['fechacuasi'], request.json['describa'], request.json['accion'], request.json['informo'], request.json['tipotrabajador']]
  # a insertar los valores
  c.execute('insert into cuasi_accidentes (cuasi_rut, cuasi_area, cuasi_equipo, cuasi_fechacuasi, cuasi_describa, cuasi_accion, cuasi_informo, cuasi_tipotrabajador) values (?,?,?,?,?,?,?,?)', params) 
  # recuperemos el último valor ingresado 
  last_id = c.lastrowid
  print("last id: " , last_id)
  conn.commit()

  conn.close()
  
  return jsonify({'id' : last_id})

# endpoint to show all users
@app.route("/api/v1/areas", methods=["GET"])
def get_areas():
  return jsonify(areas)

# endpoint to show all users
@app.route("/api/v1/equipos", methods=["GET"])
def get_equipos():
  return jsonify(equipos)

# endpoint to show all users
@app.route("/api/v1/cuasis", methods=["GET"])
def get_cuasiaccidentes():
  conn = sqlite3.connect('db/cuasiaccidente.db')
  c = conn.cursor()
  c.execute('select * from cuasi_accidentes')
  rows = c.fetchall()
  salida = []

  for row in rows:
    fila = {'id': row[0], 'rut': row[1], 'area': row[2], 'equipo': row[3], 'fechacuasi':row[4], 'describa': row[5], 'accion': row[6], 'informo': row[7], 'tipotrabajador': row[8]}
    salida.append(fila)

  return jsonify(salida)

@app.route("/api/v1/cuasis/<format>", methods=["GET"])
def get_cuasiaccidentes_format(format):
  conn = sqlite3.connect('db/cuasiaccidente.db')
  c = conn.cursor()
  c.execute('select * from cuasi_accidentes order by cuasi_id desc')
  rows = c.fetchall()

  dest = StringIO()
  writer = csv.writer(dest)
  writer.writerow(["cuasi_id","rut_reportador","area","equipo","fecha_cuasi","descripcion","accion_inm","informo_jefe","tipo_trabajador"])
  for row in rows: 
  	writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])


  output = make_response(dest.getvalue())
  output.headers["Content-Disposition"] = "attachment; filename=cuasiaccidentes-reporte.csv"
  output.headers["Content-type"] = "text/csv"
  return output



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7775, debug=True)