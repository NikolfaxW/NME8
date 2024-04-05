import numpy as np
import sys


def print_hi(name):
    print(f'Hi, {name}')

def f(x):
    result = (-1/10)*x + (1/50)*x*x + 13
    return result

def first_forward_derivation_f(x,h):
    result = f(x+h) - f(x-h)/(2*h)
    return result

if __name__ == '__main__':
    borders = np.array([-50, 50])
    tolerance = 2 * sys.float_info.epsilon
    #puleni = x/2
