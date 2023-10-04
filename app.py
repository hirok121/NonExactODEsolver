from flask import Flask, request, render_template
from First_order_ODEsolver import NonExactODEsolver
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result=''
    if request.method == 'POST':
        input1 = request.form.get('ode-input')
        checkbox = request.form.get('checkbox')
        if checkbox == 'on':
            input2 = request.form.get('input2')
            input3 = request.form.get('input3')
            result = NonExactODEsolver.masterSolver(input1, input2, input3)
        else:
            result = NonExactODEsolver.masterSolver(input1)
        return render_template('index.html', processed_text=result)
    return render_template('index.html', processed_text='')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    result=''
    if request.method == 'POST':
        input1 = request.form.get('ode-input')
        checkbox = request.form.get('checkbox')
        if checkbox == 'on':
            input2 = request.form.get('input2')
            input3 = request.form.get('input3')
            result = NonExactODEsolver.masterSolver(input1, input2, input3)
        else:
            result = NonExactODEsolver.masterSolver(input1)
        return render_template('index.html', processed_text=result)
    return render_template('form.html', processed_text='')

if __name__ == '__main__':
    app.run(debug=True)
