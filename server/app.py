#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'
    
@app.route('/count/<int:parameter>')
def count(parameter):
    results = [str(i) for i in range(parameter)]
    return '\n'.join(results) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # Use 'div' instead of '/' for the URL path
        if num2 == 0:  # Handle division by zero
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Not a valid operation."
    
    return str(result)

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
