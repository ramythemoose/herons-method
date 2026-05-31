import matplotlib.pyplot as plt
import numpy as np

def herostheorem(xn, k):
    results_list = [xn]

    while True:
        x_nplus1 = (xn + k/xn)/2
        results_list.append(x_nplus1)

        if round(x_nplus1, 5) == round(xn, 5):
            break
        else:
            xn = x_nplus1
            print(round(xn, 5))
    
    n_list = list(range(len(results_list)))
    return n_list, results_list

def plottingfunc(xn_range, xn_intervals, k_range, 
                 k_intervals, xn_start=0, k_start=1, **kwargs):
    xn = [i for i in np.linspace(xn_start, xn_range, xn_intervals) if  i != 0] 
    #generates values for xn in linspace from xn_start to xn_range, xn_intervals
    #if xn = 0, reject
    k = [i for i in np.linspace(k_start, k_range, k_intervals) if i > 0]
    #reject negative square roots

    for num in xn:
        for value in k:
            x, y = herostheorem(num, value)
            plt.plot (x, y)
    
    plt.ylabel("x_n+1")
    plt.xlabel("N convergences")
    plt.show()

plottingfunc(xn_range=5, #loop from 0 to xn_range starting guess
             xn_intervals=10, #number of points from 0 to xn_range using linspace
             k_range=1, #loop from 0 to k for sqrt(k)
             k_intervals=10, #number of points from 0 to k_range 
             xn_start=2, #starting point of xn (opt)
             k_start=-5) #starting point of k (opt)







