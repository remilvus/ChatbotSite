from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/test')
def test():
    return 'test'

@app.route('/webhook', methods=['POST'])
def respond():
    data = {"fulfillmentMessages": [
	    {
	      "text": {
		"text": [
		  "Text response from webhook"
		]
	      }
	    }
	  ]
	}
    return jsonify(data), 200


if __name__ == '__main__': app.run(debug=True)
