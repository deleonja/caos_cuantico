
from pl_data import *
import matplotlib.pyplot as plt
from numpy import linspace
plt.rcParams['text.usetex'] = True

#This function plots the eigenenergies of a system of Hamiltonian H against the expectation values of the Peres operator I, creating a Peres lattice
def peres_lattice_plot(H,I,name):
    H_Eigenenergies, I_Eigenenergies = peres_lattice_data_to_cvs(H,I,name)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlim(-400,400)
    plt.ylim(0,40)
    ax.set_xlabel('$E$')
    ax.set_ylabel(r'$\sqrt{\langle E | I^2 | E \rangle}$')
    ax.set_title(r'$\lambda = $'+f'{lam:.1f}')
    ax.scatter(H_Eigenenergies,I_Eigenenergies, color='black', marker='.')
    fig.savefig('./pyfigures/'+name+'.png')
    plt.close(fig)

for lam in linspace(0.0,10,51):
    print(f'Creating lattice for lambda = {lam:.1f} ...')
    spin_number = 20
    dimension = int(2*spin_number + 1)
    J = 1.0
    H = XY_with_field(J, lam,spin_number)
    I = qt.tensor(qt.spin_Jz(spin_number),qt.qeye(dimension)) + qt.tensor(qt.qeye(dimension),qt.spin_Jz(spin_number))
    name = f'peres_lattice_XY_with_field_lam_{lam:.1f}_s_{spin_number}'
    peres_lattice_plot(H,I,name)
