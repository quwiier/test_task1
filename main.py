from random import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def random_code():
    return random.randint(1000,9999)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
