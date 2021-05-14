import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from fit_curve_array import fit_curve_array
from lowest_eigenvectors import lowest_eigenvectors
from plot_data_with_fit import plot_data_with_fit



#1.
def parse_file_name(file_name):
  parsing = file_name.split(".")
   chemical_symbol = parsing[0]
   crystal_symbol = parsing[1]
   acronym = parsing[2]
   parse_file_name = chemical_symbol, crystal_symbol, acronym
   return parse_file_name

 file_name = "Si.Fd-3m.GGA-PBE.volumes_energies.dat"
 print(parse_file_name(file_name))


#2.
from two_column_text_read import two_column_text_read
array = two_column_text_read("/home/runner/scientific-programming-marvalena/Final_Stuff/Final_Exam/Si.Fd-3m.GGA-PBE.volumes_energies.dat")
#print(array)

#4.
from bivariate_statistics import bivariate_statistics
statistics = bivariate_statistics(array)
#print(statistics)

#5.
from quadratic_fit import quadratic_fit
quadratic_coefficients = quadratic_fit(array)
#print(quadratic_coeffients)

#6.
from equations_of_state import fit_eos
volumes = array[0, :]
energies = array[1, :]

fit_eos_array, fit_parameters = fit_eos(volumes, energies, quadratic_coefficients, eos = "murnaghan", number_of_points=50)
bulk_modulus = fit_parameters[1]
equilibrium_volume = fit_parameters[3]

#8.
plt.plot(volumes, energies, 'bo')
plt.plot(fit_volumes, fit_eos_array, 'k')
plt.xlabel(r'$\mathit{V}(\AA^3$/atom)')
plt.ylabel(r'$\mathit{E}$ (eV/atom)')


plt.show()


from generate_matrix import generate_matrix

display_graph = True
potential_name = 'square'
N_dim = 90
potential_parameter = 100

matrix = generate_matrix(-10, 10, N_dim, potential_name, potential_parameter)

#print(matrix)
eigenvalues, eigenvectors = lowest_eigenvectors(matrix, 3)
#print(eigenvalues,eigenvectors)

x = linspace(-10, 10, N_dim)  
line1, = plt.plot(x, eigenvectors[0][0:N_dim])  
line2, = plt.plot(x, eigenvectors[1][0:N_dim])  
line3, = plt.plot(x, eigenvectors[2][0:N_dim])  

plt.xlabel("x [a.u.]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.legend((line1, line2, line3), ('ψ1, Ε1 = -2.05630254 a.u.', 'ψ2, Ε2 = -0.934174  a.u.', 'ψ3, Ε3 = 0.05372449 a.u.'))
plt.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])
plt.axhline(color="black")  
plt.text(-10, -1, "Created by Marvalena DeBaere 2021/05/13") 
plt.title("Select Wavefunctions for a Square Potential on a Spatial Grid of 0, 1, 2 Points") 


if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("tada")