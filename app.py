from flask import Flask, render_template, jsonify
from spreadsheet_management import add_rhyme, add_complaint
import threading

app = Flask(__name__)


@app.route('/')
def index():
    # add_rhyme('>rhyme')
    # add_complaint('>complaint')
    # t = threading.Thread(target=add_rhyme, args=['> a rhyme'])
    # t.start()
    return render_template('index.html')
    
@app.route('/test')
def test():
    return 'test'

@app.route('/webhook', methods=['POST'])
def respond():
    # add_rhyme('>rhyme')
    # add_complaint('>complaint')
    t = threading.Thread(target=add_rhyme, args=['> a rhyme'])
    t.deamon = True
    t.start()
    data = {"fulfillmentMessages": [{"text": { "text": [ "Text response from THE webhook"]}}]}
    return jsonify(data), 200


if __name__ == '__main__': 
    app.run(debug=True)
