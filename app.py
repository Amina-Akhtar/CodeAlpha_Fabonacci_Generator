from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def fibonacci_term(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    fib_type = request.form['fibType']
    number = int(request.form['numberInput'])
    
    if number <= 0:
        return jsonify(result="You have entered an invalid number.")

    if fib_type == 'term':
        result = fibonacci_term(number)
        return jsonify(result=f"The {number}th term of the Fibonacci sequence is {result}")
    elif fib_type == 'sequence':
        result = fibonacci_sequence(number)
        result_str = ', '.join(map(str, result))
        return jsonify(result=f"The first {number} Fibonacci numbers are: {result_str}")
    else:
        return jsonify(result="Invalid option")

if __name__ == '__main__':
    app.run(debug=True)
