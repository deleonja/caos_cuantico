import numpy as np


def x(k = 1, n = 1):
    return np.kron(np.eye(2**(k-1)), np.kron(np.array([[0,1],[1,0]]), np.eye(2**(n-k))))

def y(k = 1, n = 1):
    return np.kron(np.eye(2**(k-1)), np.kron(np.array([[0,-1j],[1j,0]]), np.eye(2**(n-k))))

def z(k = 1 , n = 1):
    return np.kron(np.eye(2**(k-1)), np.kron(np.array([[1,0],[0,-1]]), np.eye(2**(n-k))))

