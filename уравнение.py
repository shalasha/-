import scipy.optimize as opt
from numpy import exp
import timeit

st1 = timeit.default_timer()

def f(variables) :
    (x,y) = variables
    first_eq = (x-3)**2 + (y-7)**2 -36
    second_eq = (x-11)**2 + (y-7)**2 -49
    return [first_eq, second_eq]

solution = opt.fsolve(f, (0.1,1) )
print(solution)


st2 = timeit.default_timer()
print("RUN TIME : {0}".format(st2-st1))
