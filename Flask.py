from flask import Flask, request, jsonify
from json_data import data

app = Flask(__name__)

@app.route('/')
def fetchAllStars():
    return jsonify({
        "Data": data,
        "Message": "Success"
    }), 200

if __name__ == '__main__':
    app.run(debug = True)