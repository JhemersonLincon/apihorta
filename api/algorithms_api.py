from algorithms.isPlanta import IsPlant
from app import app
from flask import request, jsonify
import json

@app.route("/plants/<name>", methods=['POST'])
def plants(name):
    image_upload = request.files['file']
    isPlant = IsPlant()
    if not isPlant.verificar(image_upload): 
        return jsonify({"message": "IsNotAPlant"}), 400    
    
    
    
    
    return jsonify({"message": "IsAPlant", "name": name}), 200
