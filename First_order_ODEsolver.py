import sympy as sp
import pandas as pd
import math


class NonExactODEsolver():
    nonSeparable=False
    logRemoved=False
    @staticmethod
    def masterSolver(eqn:str,x='',y=''):
        try:
            solution=''
            
            if not NonExactODEsolver.__check_validity(eqn):
                return "Equation is not valid"

            M, N, constant_value = NonExactODEsolver.reduceToStandard(eqn)
            if constant_value:
                return "This is not Ordinary Differential Equation(Constant term)"
            
            try:
                fx,fy=NonExactODEsolver.Solve(M,N)
                if NonExactODEsolver.nonSeparable:
                    return "EQn cannot be separated!!!"
            except:
                return "Make sure eqn is in right form!!!"
                
            fx_without_log,fy_without_log=NonExactODEsolver.removeLog(fx,fy) ## if possible
            if str(x) and str(y):
                x=int(x)
                y=int(y)
                if NonExactODEsolver.logRemoved:
                    c=NonExactODEsolver.initial_condition(fy_without_log/fx_without_log,x,y)
                    if isinstance(c,int):
                        solution=f"{NonExactODEsolver.__formateAnswer(fy_without_log-fx_without_log*c)} = 0"
                    else:
                        return "Cannot get particular solution with the initial condition"
                else:
                    c=NonExactODEsolver.initial_condition(fy-fx,x,y)
                    solution=f"{NonExactODEsolver.__formateAnswer(fy)} - {NonExactODEsolver.__formateAnswer(fx-c)} = 0"
            elif not str(x) and not str(y):
                if NonExactODEsolver.logRemoved:
                    solution=f"{NonExactODEsolver.__formateAnswer(fy_without_log)} = ({NonExactODEsolver.__formateAnswer(fx_without_log)})c"
                else:
                    solution=f"{NonExactODEsolver.__formateAnswer(fy)} = {NonExactODEsolver.__formateAnswer(fx)} + c"
            else:
                return "Cannot parse x,y into int."
            return solution
        except:
            return "Something very bad happened!!! i.g"
        

    @staticmethod
    def Solve(M,N):
        x,y = sp.symbols('x y')

        M,N=NonExactODEsolver.__separateVariable(M,N)
        # print("MMM ",M,"NNN ",N)
        if M and N:
            fx=sp.integrate(M,x)
            fy=sp.integrate(N,y)
            
            ###################
            # remove lcm
            fx_terms = sp.Add.make_args(fx)  # Extract terms from the fx
            fy_terms = sp.Add.make_args(fy) 
            numbers=[]
            for term in fx_terms+fy_terms:
                fraction=sp.fraction(term)
                numbers.append(fraction[1])
            # print(numbers)
            try:    
                LCM=math.lcm(*numbers)
                fx*=LCM
                fy*=LCM
                # print(LCM)
            except :
                pass

            return fx,fy 
        else:
            False,False
        
    
    @staticmethod
    def reduceToStandard(eqn: str):
        # Symbolify
        x, y,e,c,s, X, Y = sp.symbols('x y e c s X Y')
        '''
        This function f(x)g(y)dx + f'(x)g'(y)dy=0 to f(x)/f'(x)dx=-g'(y)/g(y)dy
        '''
        eqn = eqn.lower()
        eqn = eqn.replace("dx", "X")
        eqn = eqn.replace("dy", "Y")
        # eqn = eqn.replace("sin", "s")
        # eqn = eqn.replace("cos", "c")
        

        eqn = NonExactODEsolver.__add_stars(NonExactODEsolver, eqn)

        # Making Right Hand Side 0
        Lhs = eqn[0:eqn.find("=")]
        Rhs = eqn[eqn.find("=")+1:]
        LHSEq = sp.simplify(Lhs)
        RHSEq = sp.simplify(Rhs)

        Eqn = LHSEq-RHSEq
        # print(Eqn)
        ###### handle exp function
        Eqn=Eqn.subs('e',sp.E)
        # ####### handle sin/cos function
        # Eqn=Eqn.subs('s',sp.sin)
        # Eqn=Eqn.subs('c',sp.cos)
        # ########
        
        constant_value = Eqn.subs({X: 0, Y: 0})
        M =-1* sp.diff(Eqn, X) ### -1 for make it rhs
        N = sp.diff(Eqn, Y)
        
        ## Remove any fraction from M,N 
        M=sp.factor(M)
        N=sp.factor(N)
        fracM=sp.fraction(M)
        fracN=sp.fraction(N)
        M=M*fracM[1]*fracN[1]
        N=N*fracM[1]*fracN[1]
        # print("MMM ", M,"NNN",N)
        return M, N, constant_value
    

    @staticmethod
    def __separateVariable(M, N):
        x, y = sp.symbols("x,y")
        Mf = NonExactODEsolver.__getFactor(M)
        Nf = NonExactODEsolver.__getFactor(N)
        
        ###accessing static variable
        NonExactODEsolver.nonSeparable=False
        # print(" Mf ",Mf," Nf " ,Nf)

        for factor in Mf:
            ##### here we replace exp to E so that our programme dose not treat (x in exp**y) as true  
            if 'y' in str(factor).replace('exp','E') and not NonExactODEsolver.nonSeparable:
                NonExactODEsolver.nonSeparable ='y' in str(factor).replace('exp','E') and  'x' in str(factor).replace('exp','E')
                M = M/factor
                N = N/factor
        for factor in Nf:
            if 'x' in str(factor).replace('exp','E') and not NonExactODEsolver.nonSeparable:
                NonExactODEsolver.nonSeparable='y' in str(factor).replace('exp','E') and  'x' in str(factor).replace('exp','E')
                M = M/factor
                N = N/factor
        # print(nonSeparabel)
        return M, N


    @staticmethod
    def __getFactor(expression):
        factors_list = sp.factor_list(expression)
        coefficient, terms = factors_list
        result = []
        for term, power in terms:
            result.append(term ** power)
        return result

    
    @staticmethod
    def initial_condition(sol,x,y):
        sol=sol.expand()
        try:
            c=int(sol.subs({'x':x,'y':y}))
            return c
        except :
            return 'cannot get c'

###############################################################################
### Preprocess the input text

    @staticmethod
    def __check_validity(eqn: str):
        valid_char = "exyd0123456789+-*/^()= "  # space should be counted
        return all(char in valid_char for char in eqn) and "=" in eqn and len(eqn[eqn.find("=") + 1:]) 

    @staticmethod
    def __add_stars(self, input_string):
        result = []
        prev_char = ''

        for char in input_string:
            if prev_char.isalnum() and char.isalnum():
                result.append('*')
            elif prev_char == ')' and char.isalnum():
                result.append('*')
            elif prev_char == ')' and char == '(':
                result.append('*')
            elif prev_char == '(' and char == ')':
                result.append('*')
            elif prev_char.isalnum() and char == '(':
                result.append('*')

            result.append(char)
            prev_char = char

        return ''.join(result)
####################################################################
###### Post Process Output
    
    @staticmethod
    def removeLog(fx, fy):
        fx_terms = sp.Add.make_args(fx)  # Extract terms from the fx
        fy_terms = sp.Add.make_args(fy)  # Extract terms from the  fy
        
        ###accessing static variable
        NonExactODEsolver.logRemoved=False
        fx_without_log = 1
        fy_without_log = 1
        if all(['log' in str(term) for term in fx_terms+fy_terms]):
            NonExactODEsolver.logRemoved=True
            # for fx
            for term in fx_terms:
                fx_without_log *= sp.exp(term)
            ##for fy
            for term in fy_terms:
                fy_without_log *= sp.exp(term)

            return fx_without_log, fy_without_log

        return fx, fy
    
    @staticmethod
    def __create_eqn_from_str(eqn: str):
        x, y, X, Y = sp.symbols('x y X Y')
        y = sp.Function('y')(x)
        y_dot = y.diff(x)
        eqn = eqn.replace("dx", "X").replace("dy", "Y")
        eqn = NonExactODEsolver.__add_stars(
            NonExactODEsolver, eqn)  # add stars
        lhs = eqn[0:eqn.find("=")]
        rhs = eqn[eqn.find("=")+1:]
        Lhs = sp.simplify(lhs)
        Rhs = sp.simplify(rhs)
        expression = Lhs-Rhs

        # The eqn is not Exact or non_Exact ODE because of constant term.
        constant_value = expression.subs({'X': 0, 'Y': 0})

        expression = expression.subs('X', 1)
        expression = expression.subs({'y': y, 'Y': y_dot})

        return expression, constant_value

    @staticmethod
    def __create_Equation_from_roots(roots):
        y = sp.symbols('y')
        if isinstance(roots, list):
            expression = sp.Mul(*[(y - root.rhs)
                                for root in roots], evaluate=False)
        else:
            expression = y-roots.rhs
        # eqn = sp.Eq(equation, 0)
        return sp.expand(expression)  # sp.together(eqn)

    @staticmethod
    def __remove_sqrt(equation):
        x = sp.Symbol("x")
        eq_parts = equation.as_ordered_terms()

        sqrt_term = 0
        for term in eq_parts:
            if "sqrt" in str(term):
                sqrt_term = term

        if sqrt_term:
            k = 1  # sign fixer
            if sqrt_term.subs({x: 1, "C1": 1}) < 0:  # for negative sing
                k = -1

            lhs = equation-sqrt_term
            lhs = lhs*lhs
            sqrt_term = sqrt_term*sqrt_term
            equation = lhs+sqrt_term*k

        return equation
    @staticmethod
    def expTo_e(eqn):
        terms = sp.Add.make_args(eqn)
        sum=0
        for i in range(len(terms)):
            factor_list=sp.factor_list(terms[i])
            a=1
            for j in range(len(factor_list)):
                if "exp" in str(factor_list[j]):
                    factor_list[j]=sp.log(factor_list[j])
                a*=factor_list[j]
            
            sum+=terms[i]
        return sum
        
    @staticmethod
    def __formateAnswer(solution):
        
        solution = solution.cancel()
        solution = solution.factor()
        solution = solution.simplify()

        eqn = str(solution)
        eqn = eqn.replace("**", "^").replace("*","").replace("C1", "c").replace("c^2", 'c').replace("exp","e^")
        return eqn

    
    
    #######################################################################################################
    ###################### For Exact Ordinary Differential Equation#################################


    def __ExactODE(self, m, n):
        x, y, c = sp.symbols('x y c')
        # Define the coefficients M(x, y) and N(x, y)
        M = sp.simplify(m)  # Define your M(x, y) function here
        N = sp.simplify(n)   # Define your N(x, y) function here

        # Calculate partial derivatives
        M_y = sp.diff(M, y)
        N_x = sp.diff(N, x)
        # Check if the equation is exact
        if M_y == N_x:
            # If it's exact, find the potential function F(x, y)

            F = sp.integrate(M, x)  # + f(y)
            Fy = sp.diff(F, y)  # + f'(y)
            # f'(y)=N-Fy
            Y = sp.integrate(N-Fy)
            solve = F+Y
            ans = str(solve) + " = c"
            return NonExactODEsolver.formateAnswer(ans)
        else:
            return "dM/dy != dN/dx \nNot Exact ODE \nUnable to Solve"


def CSV_solve(file):
    df = pd.read_csv(file)
    ans=''
    for eqn in df['equation']:
        print(eqn)
        ans=NonExactODEsolver.masterSolver(eqn)
        print(ans)
    return
    ans = df['equation'].apply(NonExactODEsolver.masterSolver)
    # ans=NonExactODEsolver.Solve2(df['equation'][0])
    df.insert(2,"solution_by_programme",ans)
    # df.to_csv("Solve.csv",index=False)


if __name__ == "__main__":
    equation = ["(2Xy+1)dx = - (x**2 +4y)dy", "(2xy + 3y^2)dx - (2xy + x^2)dy = 0", "4xydx + (x^2+1)dy=0",
                "(x + 4)(y^2 + 1)dx + y(x^2 + 3x + 2)dy = 0", "(xy + 2x + y + 2)dx + (x^2 + 2x)dy = 0"]
    # M = "(2*x*y+1)"  # Define your M(x, y) function here
    # N = "x**2 +4*y"   # Define your N(x, y) function here
    # # print(Engine.ExactSODE(M, N))
    # # print(Engine.linear_ode())
    # print(Engine.ExactSolve(eqn))
    # Engine.makeEqn(Engine,"(2*x*y+1) = - (x**2 +4*y)-7")
    # Engine.linear_ode()
    # print(Engine.makeEqn("4xydx + (x^2+1)dy=0"))
    # y = sp.Function("y")("x")
    # x = sp.Symbol("x")
    # print(sp.classify_ode(Engine.makeEqn(eqn1),y))
    # EQn = Engine.create_eqn_from_str(eqn2)
    # print(EQn.lhs)

    # its works petty much
    # print(sp.expand(Engine.create_Equation_from_roots(sol)))

    # print(Engine.Master(eqn1))

    # sol = [NonExactODEsolver.Solve(eqn) for eqn in equation]
    sol=""
    # eqn1=" ((x-4)/x^3)dx-((y^2-3)/y^4)dy=0"
    eqn1="dy/(y+1)=dx/(x-1)"
    # sol=NonExactODEsolver.Master(eqn1)
    # print(sol)
    # sol=NonExactODEsolver.Solve(eqn1)
    print(sol)
    sol=NonExactODEsolver.masterSolver(eqn1,1,1)
    print(sol)

    # CSV_solve("problems.csv")
