from flask import Flask, request, render_template,redirect,url_for,session
from NonESODEsolver import NonExactODEsolver



app = Flask(__name__)
app.secret_key="secret_key"
solveAnother=False


@app.route('/', methods=['GET', 'POST'])
def index():
    result=''
    global solveAnother
    if request.method == 'POST':
        eqn = request.form.get('eqnField')
        session["eqn"]=eqn
        x = request.form.get('x')
        y = request.form.get('y')
        if x and y:
            result = NonExactODEsolver.masterSolver(eqn, int(x), int(y))
        else:
            result = NonExactODEsolver.masterSolver(eqn)
        session["sol"]=result
        return redirect(url_for("solution"))
    
    if solveAnother:
        solveAnother=False
        return render_template('index.html',toggleDivs="toggleDivs")
    else:
        return render_template('index.html')

@app.route('/solution', methods=['GET', 'POST'])
def solution():
    eqn=session.get("eqn")
    sol=session.get("sol")
    if request.method == 'POST':
        
        global solveAnother
        solveAnother=True
        
        return redirect('/')
    
    return render_template('solution.html',eqn=eqn,solution=sol)

@app.route('/aboutOurTeam')
def aboutOurTeam():
    return render_template('aboutOurTeam.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
