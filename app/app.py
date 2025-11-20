
from flask import Flask, jsonify, request
from calculator import add, sub, mul, div

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello from DevOps Mini Project of VAMSI!"})

@app.route('/health')
def health():
    return jsonify({"Status": "OK"})

@app.route('/calc', methods=['GET'])
def calc():
    #expects ?op=add&a=1&b=2
    op = request.args.get('op')
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({"error": "a and b must be numeric"}), 400
    
    if op == 'add':
        result = add(a, b)
    elif op == 'sub':
        result = sub(a, b)
    elif op == 'mul':
        result == mul(a, b)
    elif op == 'div':
        try:
            result = div(a, b)
        except ZeroDivisionError:
            return jsonify({"error": "division by zero"}), 400
    
    else:
        return jsonify({"error": "Invalid op"}), 400
    
    return jsonify({"Result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
