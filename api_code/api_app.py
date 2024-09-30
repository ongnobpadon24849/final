from flask import Flask, jsonify

api_app = Flask(__name__)

@api_app.route('/', methods=['GET'])
def index():
    return "SDPX GROUP 3"

@api_app.route('/is1honor/<num>', methods=['GET'])
def is1honor(num):
    try:
        num = eval(num)
        if num >= 3.50 and num <= 4.00:
            return jsonify({"Grade": num, "is1honor": True})
        elif num < 3.50 and num >= 0.00:
            return jsonify({"Grade": num, "is1honor": False})
        else:
            return jsonify({"ERROR": "Invalid input"})
    except:
        return jsonify({"ERROR": "Invalid input"})

if __name__ == '__main__':
    api_app.run(host='0.0.0.0', port=5000)
