from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('tabla-juangomez')


#Metodo para insertar elementos en una tabla de dynamodb
@app.route('/insert', methods=['POST'])
def index():
  data = request.json
  item = {**data}

  tabla.put_item(Item=item)

  return 'Se guardó exitosamente'


#Metodo para leer elementos de una tabla de dynamodb
@app.route('/get/<id>', methods=['GET'])
def get_item(id):
  try:
    response = tabla.get_item(Key={'id': id})

    if 'Item' in response:
      return jsonify(response['Item']), 200
    else:
      return jsonify({'error': 'id no existe'}), 404

  except Exception as e:
    return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
