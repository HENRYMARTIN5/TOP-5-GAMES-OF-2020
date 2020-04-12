from flask import *
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/apex')
def apex():
	return render_template("apex.html")
@app.route('/callofduty')
def callofduty():
	return render_template("callofduty.html")
@app.route('/credits')
def credits():
	return render_template("credits.html")
@app.route('/fortnite')
def fortnite():
	return render_template("fortnite.html")
@app.route('/minecraft')
def minecraft():
	return render_template("minecraft.html")
@app.route('/roblox')
def roblox():
	return render_template("roblox.html")
app.run(host='0.0.0.0', port=8080)