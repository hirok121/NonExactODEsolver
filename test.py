from sympy import *
import sympy as sp
import pandas as pd
import math


class NonExactODEsolver():
        
    
    @staticmethod
    def reduceToStandard(eqn: str):
        x, y,e,c,s, X, Y = sp.symbols('x y e c s X Y')
        eqn = eqn.lower()
        print("EQN 1 ",eqn)
        eqn = eqn.replace("dx", "X")
        eqn = eqn.replace("dy", "Y")
        eqn = eqn.replace("sin", "s")
        eqn = eqn.replace("cos", "c")
        print("EQN 2 ",eqn)
        
        eqn = NonExactODEsolver.__add_stars(NonExactODEsolver, eqn)
        print("EQN 3 ",eqn)
        eqn = eqn.replace("s", "sin")
        eqn = eqn.replace("c", "cos")
        print("EQN 4 ",eqn)

        Lhs = eqn[0:eqn.find("=")]
        Rhs = eqn[eqn.find("=")+1:]
        LHSEq = sp.simplify(Lhs)
        RHSEq = sp.simplify(Rhs)

        Eqn = LHSEq-RHSEq
        Eqn=Eqn.subs('e',sp.E)
        print("EQN 5 ",Eqn)
        print("////////////////////////")        
        constant_value = Eqn.subs({X: 0, Y: 0})
        M =-1* sp.diff(Eqn, X) 
        N = sp.diff(Eqn, Y)
    
        ########## Check output for M and N ###########
        print(f"M = {M}")
        sol2 = integrate(M)
        print(f"M Integrated = {sol2}")

        print(f"N = {N}")
        sol3 = integrate(N)
        print(f"N Integrated = {sol3}")
     



        M=sp.factor(M)
        N=sp.factor(N)
        fracM=sp.fraction(M)
        fracN=sp.fraction(N)
        M=M*fracM[1]*fracN[1]
        N=N*fracM[1]*fracN[1]
        

        return M, N, constant_value

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

            ######### Modified here #########
            elif prev_char.isalnum() and prev_char != 'c' and prev_char != 's' and char == '(':
                result.append('*')

            result.append(char)
            prev_char = char

        return ''.join(result)
    
    
if __name__ == "__main__":
    s=sp.simplify("cos(x)")
    print(type(s))
    eqn1="(cos(x+3x^2)/sin(x)+cos(x))dx=-(e^y/(1+e^y))dy"
    sol=NonExactODEsolver.reduceToStandard(eqn1)


