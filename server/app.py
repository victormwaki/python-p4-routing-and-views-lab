#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(f"Recieved string: {parameter}")

    return f"String recieved and printed: {parameter}"

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ",".join(str(num) for num in range(1, parameter + 1))
    return f"<pre>{numbers}</pre>"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == '+':
        reslut = num1 + num2
    elif operation == '-':
            reslut = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
    #check for division
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        #check for modulus by zero
        if num2 == 0:
            return "Error: Moduls by zero is not allowed."
        result = num1 % num2
    else:
        return f"Error: Unsupported operation '{operation}'. Use one of +, -, *, div, %."
    #return the result as a responce
    return f"The result of {num1} {operation} {num2} is: {result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
