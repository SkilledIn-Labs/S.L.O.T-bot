from flask import Flask, request
from src.vaccine import generate_and_save_token
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/mobile')
def mobile():
    mob = request.args.get('mobile')
    generate_and_save_token(mob)
    return 'Done!'


if __name__ == '__main__':
    app.run()
