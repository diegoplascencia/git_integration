from flask import Flask 

app = Flask(__name__) #unique name

@app.route('/') #Home direction
def home_method():
	return "First Flask MF"

app.run(port=5000)