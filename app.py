from flask import Flask 

app = Flask(__name__) #unique name

@app.route('/') #Home direction
def hello():
	return "Hello World"

app.run(port=5000)