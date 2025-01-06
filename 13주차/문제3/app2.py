from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.errorhandler(500)

def page_not_found(error) :
	return "<h1> 500 Error</h1>", 500

if __name__ == '__main__' :
	app.run(debug=True)