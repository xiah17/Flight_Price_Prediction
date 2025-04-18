from flask import Flask, request, jsonify
import pickle
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask (__name__)
CORS(app)

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Dictionaries For Categorical Variables
