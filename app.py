import pickle
from flask import Flask, request, jsonify, abort
import logging
import numpy as np
app = Flask(__name__)          
app.logger.setLevel(logging.DEBUG)
import warnings
warnings.filterwarnings('ignore')

with open('crop_recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

def class_predict(x):
    out = encoder.inverse_transform(model.predict(np.array(x).reshape(1, -1)))[0]
    return out

@app.route('/')
def home():
    return "Home"

@app.route("/plant/crop_recommendation", methods=['POST', 'GET'])
def test_method():
    if request.method == 'GET':
        return {"code":201}
    # print(request.json)     
    # if not request.json or 'data' not in request.json: 
    #     abort(400)
    data = request.json['data']
    print(data)
    keys = ['N', 'P', 'K', 'temperature', 'humidity', 'ph']

    x = [data[key] for key in keys]

    label = class_predict(x)

    return jsonify({"prediction": label})
    
def run_server_api():
    app.run(host="0.0.0.0")


if __name__ == "__main__":     
    run_server_api()


    

