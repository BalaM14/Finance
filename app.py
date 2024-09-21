from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellow():
    return "Hello world"

@app.route('/hey')
def hello():
    return "Hello bala"

if __name__ == "__main__":
    app.run(debug=True)