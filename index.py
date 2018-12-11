import json

from flask import Flask, send_from_directory
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
def root():
    return send_from_directory('', 'index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/topic', methods=['GET'])
def get_topics():
	return json.dumps({"topics": ['javascript', 'python']})

if __name__ == '__main__':
    app.run(debug=True)
