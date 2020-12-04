from flask import Flask, render_template, jsonify
from spreadsheet_management import add_rhyme, add_complaint
import threading

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def respond():
    add_rhyme("AAAAAAAAAAAAAA")
    data = {"fulfillmentMessages": [{"text": { "text": [ "Text response from THE webhook"]}}]}
    return jsonify(data), 200


if __name__ == '__main__': 
    app.run(debug=True)
