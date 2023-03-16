from flask import Flask

app = Flask(__name__)


@app.route('/all_methods', methods=['GET'])
def all_methods():
    future_possibilities = ['/post_my_wisdom', '/delete_my_humble_opinion', '/get_Statham_confidence']
    return future_possibilities

