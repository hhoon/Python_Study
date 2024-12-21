from flask import Flask

app = Flask(__name__)

@app.route('/home/<pagename>')
def helloworld(pagename):
	return 'Hello, ' + pagename + '!'

if __name__ == '__main__' :
	app.run(debug=True)