from matplotlib import pylab
import pylab as plt
import numpy as np
import os,sys

"""
A function used for neural network activation
in artifacial intelligence, machine learning
"""

def sigmoid(x):
    #f(x)=1/(1+e^(-x))
    return (1 / (1 + np.exp(-x)))

def sigmoidplot():
    x = plt.linspace(-10,10,5)
    y = plt.linspace(-10,10,10)
    z = plt.linspace(-10,10,100)

    plt.plot(x, sigmoid(x), 'r', label='linspace(-10,10,5)')
    plt.plot(y, sigmoid(y), 'b', label='linspace(-10,10,10)')
    plt.plot(z, sigmoid(z), 'y', label='linspace(-10,10,100)')


    plt.title('Sigmoid Function')
    plt.suptitle('Math')
    plt.grid()
    plt.legend(loc='lower right')
    plt.text(-9,0.8, r'$\sigma(x)=\frac{1}{1+e^{-x}}$', fontsize=15)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(2))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.show()

def main():
    if "-a" in sys.argv[1:]:
        for i in range(-5,5):
           print(sigmoid(i))
    elif "-p" in sys.argv[1:]:
        sigmoidplot()
    else:
        for i in range(-5,5):
           print(sigmoid(i))
        sigmoidplot()
        

if __name__=="__main__":
    main()

