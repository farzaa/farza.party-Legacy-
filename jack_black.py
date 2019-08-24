from flask import Flask
from flask import render_template
from flask import send_from_directory

import os

app = Flask(__name__)

root_dir = os.path.dirname(os.getcwd())

@app.route("/")
def meme_page():
    return send_from_directory(".", 'elongated_musk.html')

@app.route("/reviews")
def trash():
    return send_from_directory(".", "love.html")

@app.route("/reviews/<page>")
def specificTrash(page=None):
    return send_from_directory(".", f"garbanzo/{page}.html")

@app.route("/notes/<page>")
def specificPasta(page=None):
    return send_from_directory(".", f"garbanzo/notes_{page}.html")

# Dev Mode: FLASK_APP=jack_black FLASK_DEBUG=1 python -m flask run
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)