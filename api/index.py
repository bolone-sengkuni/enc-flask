from flask import Flask
from flask import request
from flask import jsonify
from kunci import *



app = Flask(__name__)

@app.route("/",  methods = ['GET'])
def home():
    return jsonify(
        author="Bolone sengkuni",
    )


@app.route('/api/encrypt', methods=['GET'])
def encrypt():
    data = request.args.get('data')
    try:
        hasil = Kunci().encrypt(data=data).decode("utf-8")
        return jsonify(
            code=200,
            hasil=hasil
        )
    except:
        return jsonify(
            code=405,
            hasil="error"
        )

@app.route('/api/decrypt', methods=['GET'])
def decrypt():
    data = request.args.get('data')
    data = data.replace(" ", "+")
    try:
        hasil = Kunci().decrypt(data=data)
        return jsonify(
            code=200,
            hasil=hasil
        )
    except:
        return jsonify(
            code=405,
            succes=False,
            hasil="error"
        )


if __name__ == "__main__":
    app.run()
