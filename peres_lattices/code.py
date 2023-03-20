import numpy as np
import pauli
import qutip as qt



def XY_with_field(J, lam):
    n = 2
    return -J*(np.matmul(pauli.x(1, n), pauli.x(2, n)) + np.matmul(pauli.y(1, n), pauli.y(2, n)))+ lam*(pauli.x(1,n) + pauli.x(2, n))

print(np.array(qt.spin_Jz(5)))