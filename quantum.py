#Code for Formulas in Quantum Mechanics

import math

global h
h = 6.62*(10**(-34))

global c
c = 2.9*(10**8)

global u0
u0 = 4*(math.pi)*10**(-7)

global kB
kB = 1381*10**(-7)

global emass
emass = 9.11*10**(-31)

def bohr_model(E1,E2):
    E = E1-E2
    f = E/h
    return f

def compton_scattering(m,theta):
    s = (h/(m*c))*(1-math.cos(theta))
    return s

def compton_wavelength(m):
    w = h/(m*c)
    return w

def curie_constant(N,a,u):
    cu = (u0/(3*kB))*(N/((a**3)*(u**2)))
    return cu

def de_broglie_wavelength(m,v,p):
    de = h/(m*v)
    return de

def hydrogen_energy(n,z):
    E = -emass*(c**2)*((1/137)**2)*z/(2*(n**2))
    return E

def photoelectric_effect(f,f0):
    KE = h*(f-f0)
    if KE >= 0:
        return KE
    else:
        Q = "Photoelectric effect will not occur. Maximum K.E is less than Zero."
        return Q

def photon_energy(w):
    PE = (h*c)/w
    return PE

def rydberg_eqn(z,n1,n2):
    R = 1.097*10**7
    v = 1/(R*(z**2)*((1/(n2**2))-(1/(n1**2))))
    return v

def stefan_boltzmann(a,t,e):
    SBC = 5.67*(10**(-8))
    RP = SBC*e*a*(t**4)
    return RP

def wein_law_pw(bbt):
    b = 2.8977719
    pw = b/bbt
    return pw

def wein_law_pf(bbt):
    k = 5.87*(10**10)
    pf = k*bbt
    return pf