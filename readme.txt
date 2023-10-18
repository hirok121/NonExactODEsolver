Non-Exact Separable ODE Solver Description
The non_exact_separable_ode_solver.py program is designed to solve non-exact separable ordinary differential equations (ODEs) in a specific format. Here's how the equation should be structured:
•	The equation should be in the form of (M(x,y)dx + N(x,y)dy=0).
•	Replace M(x,y) and N(x,y) with the expressions that define your ODE.
•	Optionally, you can specify initial conditions for x and y . Provide these initial conditions as x and y variables in the code if needed.
The primary function, masterSolver(eqn, x='', y=''), takes the ODE equation and, optionally, initial conditions as input. It attempts to solve the non-exact separable ODE and provides the solution.
Other functions briefly described:
•	Solve(M, N): Attempts to solve the ODE by separating variables and performing integration.
•	replaceSubStr(eqn): Handles string substitutions for trigonometric functions and formatting.
•	reduceToStandard(eqn): Transforms the input equation into a standard form suitable for solving.
•	removeLog(fx, fy): Attempts to remove logarithmic terms from fx and fy for simplification.
•	initial_condition(sol, x, y): Determines the particular solution using initial conditions, if provided.
•	expTo_e(eqn): Converts "exp" to "e^" in the equation for better representation.
•	formateAnswer(solution): Formats the solution string for consistency.
The program processes the equation and displays the solution in the console.

Please make sure to structure your non-exact separable ODE according to the provided format for successful usage.
Thx.


