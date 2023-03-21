import qutip as qt
from math import sqrt
from os import path
from numpy import savetxt, genfromtxt,array

# This is the Hamiltonian for the XY model with a magnetic field
# I took this from 'The transition to chaos' by Linda Reichl. p.280'
def XY_with_field(J, lam,spin_number):
    dimension = int(2*spin_number + 1)
    # Interaction term
    Hxy = -J*(qt.tensor(qt.spin_Jx(spin_number),qt.spin_Jx(spin_number)) + qt.tensor(qt.spin_Jy(spin_number),qt.spin_Jy(spin_number))) 
    # Magnetic field term
    Hf = lam*(qt.tensor(qt.spin_Jx(spin_number),qt.qeye(dimension)) + qt.tensor(qt.qeye(dimension),qt.spin_Jx(spin_number)))
    # Return the total Hamiltonian
    return Hxy + Hf

def XY_single_site_anisotropy(a,spin_number):
    dimension = int(2*spin_number + 1)
    # Interaction term
    Hxy = -(qt.tensor(qt.spin_Jx(spin_number),qt.spin_Jx(spin_number)) + qt.tensor(qt.spin_Jy(spin_number),qt.spin_Jy(spin_number))) 
    # Magnetic field term
    Hf = -0.5*a*(qt.tensor(qt.spin_Jx(spin_number),qt.qeye(dimension))**2+qt.tensor(qt.qeye(dimension),qt.spin_Jx(spin_number))**2-qt.tensor(qt.spin_Jy(spin_number),qt.qeye(dimension))**2-qt.tensor(qt.qeye(dimension),qt.spin_Jy(spin_number))**2)
    # Return the total Hamiltonian
    return Hxy + Hf


#This function returns the eigenenergies of a system of Hamiltonian H, along with the expectation values of the Peres operator I
def peres_lattice_data(H,I):
    H_Eigenenergies , H_Eigenstates = H.eigenstates()
    I_Eigenenergies = [sqrt(qt.expect(I*I,h_eigenstate)) for h_eigenstate in H_Eigenstates]
    return H_Eigenenergies, I_Eigenenergies

#This function just saves the data from peres_lattice_data to a csv file so that it can be used by pl_plots.py
def peres_lattice_data_to_cvs(H,I,name):
    #Checks if the file exists
    print('Checking if file exists...')
    if path.exists('./data/'+name+'.csv'):
        print('File exists, loading data...')
        return genfromtxt('./data/'+name+'.csv', delimiter=",")
    else:
        print('File does not exist, creating data...')
        data = peres_lattice_data(H,I)
        savetxt('./data/'+name+'.csv', data, delimiter=",")
        return array(data)
    
def main():
    spin_number = 20
    dimension = int(2*spin_number + 1)
    J = 1.0
    H = XY_with_field(J, 0.0,spin_number)
    I = qt.tensor(qt.spin_Jz(spin_number),qt.qeye(dimension)) + qt.tensor(qt.qeye(dimension),qt.spin_Jz(spin_number))
    name = f'peres_lattice_XY_with_field_lam_{0.0}_s_{spin_number}'
    peres_lattice_data_to_cvs(H,I,name)

if __name__ == '__main__':
    print('Code running...')
    main()