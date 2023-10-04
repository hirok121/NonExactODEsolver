from flask import Flask, request, render_template,redirect,url_for,session
from First_order_ODEsolver import NonExactODEsolver
app = Flask(__name__)
app.secret_key="secret_key"
@app.route('/', methods=['GET', 'POST'])
def index():
    result=''
    if request.method == 'POST':
        eqn = request.form.get('eqnField')
        session["eqn"]=eqn
        x = request.form.get('x')
        y = request.form.get('y')
        if x and y:
            result = NonExactODEsolver.masterSolver(eqn, int(x), int(y))
            return redirect("/solution/")
            return render_template('index.html', processed_text=result)
        else:
            result = NonExactODEsolver.masterSolver(eqn)
            return redirect(url_for("solution"))
    return render_template('index.html')

@app.route('/solution', methods=['GET', 'POST'])
def solution():
    # eqn = request.args.get('eqn')
    # age = request.args.get('age')
    eqn=session.get("eqn")
    return render_template('solution.html',eqn=eqn)

if __name__ == '__main__':
    app.run(debug=True)
