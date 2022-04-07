from PIL import Image, ImageDraw
import scipy.optimize as opt
from numpy import exp
import timeit

st1 = timeit.default_timer()

def f(variables) :
    (x,y) = variables
    first_eq = (x-3)**2 + (y-7)**2 -36
    second_eq = (x-11)**2 + (y-7)**2 -49
    return [first_eq, second_eq]

solution_x, solution_y = opt.fsolve(f, (0.1,1) )
print(solution_x, solution_y)

st2 = timeit.default_timer()
print("RUN TIME : {0}".format(st2-st1))

# Пустой желтый фон.
im = Image.new('RGB', (500, 300), (219, 193, 27))
draw = ImageDraw.Draw(im)

draw.point((3, 7), fill='blue')
draw.point((11,7), fill='blue')
draw.point((solution_x, solution_y), fill='red')


#im.save("graphic.png", "PNG")
im.show()
