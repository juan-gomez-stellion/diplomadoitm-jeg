from flask import Flask, request
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('tabla-juangomez')


@app.route('/insert', methods=['POST'])
def index():
  data = request.json
  item = {**data}

  tabla.put_item(Item=item)

  return 'Se guardó exitosamente'


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
