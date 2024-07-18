#from flask import Flask
from flask import Flask, render_template, request
from markupsafe import escape
from flask_cors import CORS
#from requests import request

app = Flask(__name__)
CORS(app)

# @app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"

#@app.route("/<somename>")
#def hello_world(somename):
#    return f"Hello, {escape(somename)}!"

@app.route('/')
def hello():
    return 'Hello, base'



#@app.route('/hello')
#def hello():
#    return 'Hello, World'

@app.route('/login', methods=['GET', 'POST'])
def login():
#    if request.method == 'POST':
#        return 'You POSTed to login'
#    else:
#    	return f"requested to, {escape(request.method)}"
	return {
		"yourmethod": request.method
	}

#if __name__ == "__main__":
#app.run(debug=True)