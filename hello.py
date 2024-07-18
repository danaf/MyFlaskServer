#from flask import Flask
from flask import Flask, render_template, request
from markupsafe import escape
from flask_cors import CORS
#from requests import request
#from gpu_utils import gpu_init
#import torch
#import tensorflow as tf

app = Flask(__name__)



@app.route('/')
def hello():
	return 'Hello, World'



