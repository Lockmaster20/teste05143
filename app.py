from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('Diogo Fernandes.')

app.run(debug=True)
