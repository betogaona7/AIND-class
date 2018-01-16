import numpy as np

"""
	Function that takes as input a list of numbers,
	and returns the list of values given by the 
	softmax function.
"""
def softmax(L):
	expL = np.exp(L)
	return np.divide(expL, expL.sum())

"""
	Function that takes as input two lists Y, P, and
	returns the float corresponding to their cross 
	entropy.
"""
def cross_entropy(Y, P):
	Y = np.float_(Y)
	P = np.float_(P)
	return -np.sum(Y*np.log(P) + (1-Y)*np.log(1-P))