#from flask import Flask
from flask import Flask, render_template, request
from markupsafe import escape
from flask_cors import CORS
#from requests import request
#from gpu_utils import gpu_init
#import torch
#import tensorflow as tf

app = Flask(__name__)

print("This is a test v2")

@app.route('/')
def hello():
	return 'Hello, World v2'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)
