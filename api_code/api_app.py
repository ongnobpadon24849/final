from flask import Flask, jsonify

api_app = Flask(__name__)

@api_app.route('/', methods=['GET'])
def index():
    return "SDPX GROUP 3"

@api_app.route('/mul5/<num>', methods=['GET'])
def mul5(num):
    try:
        num = eval(num)
        out = f'{num*5}'
        return jsonify({"result": out})
    except:
        return jsonify({"ERROR": "Invalid input"})

if __name__ == '__main__':
    api_app.run(host='0.0.0.0', port=5000)
