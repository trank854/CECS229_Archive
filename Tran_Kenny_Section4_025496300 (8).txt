#Kenny Tran 025496300
#CECS229 Lab 7
#5/5/21

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def least_sq(file_name):
    df1 = pd.read_csv(file_name)
    xtot = 0
    xsq = 0
    ytot = 0
    xytot = 0
    n = len(df1['x'])
    for x in df1['x']:
        xtot += x
    for x2 in df1['x']:
        xsq += x2**2
    for y in df1['y']:
        ytot += y
    for z in df1:
        a = df1['x']*df1['y']
    for b in a:
        xytot += b
    m = (n*xytot-xtot*ytot)/(n*xsq-xtot**2)
    b = (ytot - m * xtot)/n
    m = round(m,4)
    b = round(b,4)
    return m, b

def mat_least_sq(file_name):
    df1 = pd.read_csv(file_name)
    listX = []
    listy = []
    mb = []
    matrix1 = np.ones(len(df1['x']))
    for x in df1['x']:
        listX.append(x)
    for y in df1['y']:
        listy.append(y)
    matrixX = np.array(listX)
    matrixy = np.array(listy)
    matrixX = np.column_stack((matrixX,matrix1))
    Xt = matrixX.T
    Xtx = np.dot(Xt,matrixX)
    Xtxinv = np.linalg.inv(Xtx)
    Xty = np.dot(Xt,matrixy)
    mbold = np.dot(Xtxinv,Xty)
    for x in mbold:
        c = round(x,4)
        mb.append(c)
    mb = np.array(mb)
    return mb

def plot_reg(file_name, using_matrix):
    df1 = pd.read_csv(file_name)
    if(using_matrix == True):
        m,b = mat_least_sq(file_name)
        plt.title('Using Matrix Least Square')
    else:
        m,b = least_sq(file_name)
        plt.title('Using Algebra Least Square')
    plt.xlabel('x')
    plt.ylabel('y')
    
    np_x = df1['x'].to_numpy()
    np_y = df1['y'].to_numpy()
    yslope = m*np_x + b
    x = np_x
    y = np_y
    plt.scatter(x,y,color = 'red',label='Data Points', marker = 'x')
    plt.plot(x,yslope,color='black',label='Line of Best Fit',linestyle='solid')
    plt.legend()
    plt.show()
