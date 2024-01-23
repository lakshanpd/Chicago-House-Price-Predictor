from flask import Flask, request, jsonify

import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
   data = request.get_json()
   Bedroom = float(data['Bedroom'])
   Space = float(data['Space'])
   Room = float(data['Room'])
   Bathroom = float(data['Bathroom'])
   Garage = float(data['Garage'])
   Condition = float(data['Condition'])

   response = jsonify({
      'estimated_price':util.predict_price(Bedroom, Space, Room, Bathroom, Garage, Condition)
   })
   response.headers.add('Access-Control-Allow-Origin', '*')
   return response

if __name__ == '__main__':
   util.load_saved_artifacts()
   app.run(port=5001)