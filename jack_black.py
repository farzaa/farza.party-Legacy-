from flask import Flask
app = Flask(__name__)

@app.route("/")
def meme_page():
    return "what??"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)