import scipy.constants as scconst
import math
import numpy as np

import matplotlib.pyplot as plt

#(4/4points for task 4)

# (a) plot distribution, plot is included in solution
# siliciumdioxid
m_mol = 60.1 #g/mol
#mol = 6.02214076e23
m_kg = m_mol / scconst.Avogadro / 1000
print(m_kg)

t_c = 1450 #K

#Stickstoff
#m_u = 14
#print(m_u * scconst.atomic_mass)

def velocity_dist(v, m, T):
    a = math.pow(m/(2 * scconst.pi * scconst.Boltzmann * T), 3/2) * 4 * scconst.pi
    b = m / (2 * scconst.Boltzmann * T)
    v_sq = np.power(v, 2)
    d = a * v_sq * np.exp(-b * v_sq)
    return d

"""
lin = np.linspace(0, 3000, 3000)
plt.plot(lin, velocity_dist(lin, m_kg, t_c), label="T = 1450K")
plt.xlabel("v [m/s]")
plt.ylabel("p(v)")
plt.title("Maxwell-Boltzmann velocity distribution for SiO2")
plt.legend()
plt.savefig("Sh2_Ex4_a")
plt.show()
"""

# (d) thermal de Broglie wavelength for SiO2
lambda_t = scconst.h / math.sqrt(2 * math.pi * m_kg * scconst.Boltzmann * t_c)
print(lambda_t) # 5.9139638837803536e-12 meters
print(lambda_t / 1e-10) # 0.059139638837803536
