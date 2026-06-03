import matplotlib.pyplot as plt
import numpy as np
import tabulate as tabulate
import pandas as pd

np.set_printoptions(legacy='1.25') #stops the annoying npfloat64 output for printing floats in a list

def herostheorem(xn, k):
    results_list = [xn]

    while xn != 0:
        x_nplus1 = (xn + k/xn)/2
        results_list.append(x_nplus1)

        if round(x_nplus1, 3) == round(xn, 3):
            break
        else:
            xn = x_nplus1
        if xn == 0: 
            print(f"You cannot divide by zero!")
            break #break algorithm if xn == 0
    
    n_list = list(range(len(results_list)))
    
    results_df = pd.DataFrame(n_list,
                              results_list)
    print(tabulate.tabulate(results_df, headers=("X_n","Convergence Step"), tablefmt="grid"))
    #create a table for fixed xn and k values and show convergence steps
    print(f"The square root of {k} is {results_list[-1]:.3f} to 3 decimal places.\n From x_0 = {results_list[0]}, it took {len(n_list)-1} steps to converge.")

    return n_list, results_list

def plottingfunc(xn_range, k_range, xn_intervals,
                 k_intervals, xn_start, k_start):
    xn = [i for i in np.arange(xn_start, xn_range+1, xn_intervals) if  i != 0] 
    #list of values for xn in linspace from xn_start to xn_range, xn_intervals. list comp because generators hate loops
    #if xn = 0, reject for k/xn = undefined
    k = [j for j in np.arange(k_start, k_range+1, k_intervals) if j > 0]
    #reject negative square roots
    
    for i in xn: #loop over xn list
        for j in k: #loop over k list
            n_list, results_list = herostheorem(i, j) #calculate heros theorem for each value of xn over a range of k values
            plt.plot(n_list, results_list, marker='o', ms = 2) #plot convergence steps against values for x0
            print(n_list, results_list)
            print(i, j)
            

    interface_txt = f"Plotting: \nk: {k_start} -> {k_range} in steps of {k_intervals} \nxn: {xn_start} -> {xn_range} in steps of {xn_intervals}"
    print(interface_txt, end='')

    plt.xlabel("Convergence steps")
    plt.ylabel("Values of x0")
    plt.title("Convergence steps for each x0")
    plt.show()

def plot_varxn_fixedk(xn_start, xn_range, xn_intervals, k):
    fixedk_plot = plottingfunc(xn_range=xn_range, 
            xn_intervals=xn_intervals, 
            k_range=k, 
            k_intervals=1, 
            xn_start=xn_start, 
            k_start=k) 
    
    return fixedk_plot #variable xn range, fixed k plot

def plot_fixedxn_vark(k_start, k_range, k_intervals, xn):
    fixedxn_plot = plottingfunc(xn_range=xn,
            xn_intervals=1, 
            k_range=k_range, 
            k_intervals=k_intervals, 
            xn_start=xn, 
            k_start=k_start) 
    
    return fixedxn_plot #fixed xn, variable k plot

def plot_varxn_vark(xn_start, xn_range, xn_intervals, k_start, k_range, k_intervals):
    varall_plot = plottingfunc(xn_range=xn_range, 
            xn_intervals=xn_intervals, 
            k_range=k_range, 
            k_intervals=k_intervals, 
            xn_start=xn_start, 
            k_start=k_start) 
    
    return varall_plot #variable xn range, variable k plot

def plot_fixedxn_fixedk(xn, k):
    fixedall_plot = plottingfunc(xn_range=xn, 
            xn_intervals=1, 
            k_range=k, 
            k_intervals=k, 
            xn_start=xn, 
            k_start=k)
    
    return fixedall_plot #fixed xn, fixed k plot
    
#herostheorem(10.3, 99.9)
#plot_varxn_fixedk(0, 10, 2, k=100)
#plot_fixedxn_vark(0, 10, 2, xn=100)
plot_varxn_vark(0, 100, 10, 0, 100, 10)
#plot_fixedxn_fixedk(8, 100)
    








