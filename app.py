from flask import Flask, render_template, jsonify, request
from spreadsheet_management import add_rhyme, add_complaint, save_rhyme_to_file, load_rhyme_from_file
import threading

app = Flask(__name__)
save_rhyme_to_file(wait=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def respond():
    data = request.get_json(silent=True)
    request_type = data['queryResult']['intent']['displayName']
    
    if request_type == 'Complaint':
        request_content = data['queryResult']['parameters']['any']
        add_complaint(request_content)
        reply = {
            "fulfillmentText": "Żałujemy, że Cię to spotkało. Postaramy się poprawić.",
        }
        return jsonify(reply), 200

    elif request_type == 'Rhyme':
        request_content = data['queryResult']['parameters']['any']
        add_rhyme(request_content)
        reply = {
            "fulfillmentText": "Piękna przyśpiewka, zostanie dodana do naszej kolekcji :D",
        }
        return jsonify(reply), 200
        
    elif request_type == 'GetRhyme':
        rhyme = load_rhyme_from_file()
        save_rhyme_to_file()
        reply = {
            "fulfillmentText": rhyme,
        }
        return jsonify(reply), 200

    reply = {"fulfillmentText": "Coś poszło nie tak - nie rozumiem o co chodzi",}
    return jsonify(reply), 200


if __name__ == '__main__': 
    app.run(debug=True)
