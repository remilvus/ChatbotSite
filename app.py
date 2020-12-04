from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    print("this is a webhook")
    return Response(status=200)


if __name__ == '__main__': app.run(debug=True)
