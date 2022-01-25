#Kenny Tran 025496300
#CECS229 Lab 5
#3/26/21
import numpy as np

def per_to_dec(mat):
    dec = mat/100
    return dec

def sig_change(oldmat, newmat):
    othermat = oldmat - newmat
    for a in othermat:
        for b in a:
            if (b < 0):
                b = -1*b
            if (b >= 0.0001):
                return True
    return False

def prob_x(mat, x):
    decmat = per_to_dec(mat)
    newmat = decmat
    for a in range(x-1):
        newmat = np.dot(newmat,decmat)
    return newmat

def long_run_dist(probs):
    dec = per_to_dec(probs)
    dec2 = dec
    while(1):
        newdec = np.dot(dec, dec2)
        condition = sig_change(dec2, newdec)
        if (condition == False):
            return newdec
        else:
            dec2 = newdec