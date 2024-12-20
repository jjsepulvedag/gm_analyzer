"""
--------------------------------------------------------------------------------
PURPOSE:
Computation of the pseudo spectral acceleration given an earthquake ground motn.
--------------------------------------------------------------------------------
FUNCTIONS:
    - newmarkB_constAcc(): Newmark Beta method, constant acceleration 
    (gamma=1/2, beta=1/4)
    - newmark_beta_linear(): Newmark Beta method, linear acceleration 
    (gamma=1/2, beta=1/6)
--------------------------------------------------------------------------------
NOTES:
    - Constant acceleration: unconditionally stable. gamma=1/2, beta=1/4
    - Linear acceleration: stable when dt/Tn < 0.551. gamma=1/2, beta=1/6
    Which is better? Linear acceleration is more accurate (linear interpolation 
    is more real than a constant acceleration), but constant acceleration is 
    stable always.  

    - omega_n = np.sqrt(k / m)
    - c = xi * (2 * m * omega_n)

--------------------------------------------------------------------------------
REFERENCES:
    - Chopra, A.K. (2007) Dynamic of Structures, Theory and Applications to 
    Earthquake Engineering. 3rd Edition, Prentice Hall, Upper Saddle River. 
"""

import numpy as np
import gm_formatSeries
import matplotlib.pyplot as plt

def newmarkB_constAcc(pt, t, delta_t, m, c, k, u_0, dudt_0):
    '''
    gamma = 1/2; beta=1/4
    INPUT:
        - pt      : an array giving the discretized load p(t) (in the case of an 
                    earthquake base excitation pt = -m*acc(t))
        - t       : time points for the computation of u(t)
        - delta_t : time step
        - m       : Mass of the system
        - c       : Damping coefficient of the system
        - k       : Elastic stiffness of the system
        - u_0     : initial displacement
        - dudt_0  : initial velocity
    OUTPUT:
        - u       : The computed displacement with time
    '''
    # ------------------------------------------------------------------------ #
    #                            Initial conditions                            #
    # ------------------------------------------------------------------------ #
    # Constants for the Newmark Beta method constant acceleration
    gamma = 1/2
    beta = 1/4

    # Vectors for storing the response
    u      = np.zeros_like(pt)
    dudt   = np.zeros_like(pt)
    d2udt2 = np.zeros_like(pt)

    # Initial computations
    d2udt2_0 = (1/m)*(pt[0] -c*dudt_0 - k*u_0)
    k_bar = k + m/(beta*delta_t**2) + c*gamma/(beta*delta_t)
    a = c*gamma/beta + m/(beta*delta_t)
    b = m/(2*beta) + c*delta_t*(gamma/(2*beta) - 1)

    # Initial values
    t[0]      = 0
    u[0]      = u_0
    dudt[0]   = dudt_0
    d2udt2[0] = d2udt2_0

    # ------------------------------------------------------------------------ #
    #                        For loop for each time step                       #
    # ------------------------------------------------------------------------ #

    u_i      = u[0]
    dudt_i   = dudt[0]
    d2udt2_i = d2udt2[0]

    for i in range(1, pt.size):
        delta_p_i = pt[i] - pt[i - 1]
        delta_p_ibar = delta_p_i + a*dudt_i + b*d2udt2_i
        delta_u_i = delta_p_ibar/k_bar
        delta_dudt_i = ((gamma/(beta*delta_t))*(delta_u_i-dudt_i*delta_t) + 
                     (1-gamma/(2*beta))*d2udt2_i*delta_t)
        delta_d2udt2_i = ((1/(beta*delta_t**2))*(delta_u_i - dudt_i*delta_t) - 
                          (1/(2*beta))*d2udt2_i)
        
        # Storing values for the iteration i
        t[i]      = t[i - 1] + delta_t
        u[i]      = u[i - 1] + delta_u_i
        dudt[i]   = dudt[i - 1] + delta_dudt_i
        d2udt2[i] = d2udt2[i - 1] + delta_d2udt2_i

        # New values for the next iteration
        u_i = u[i]
        dudt_i = dudt[i]
        d2udt2_i = d2udt2[i]
    
    # ------------------------------------------------------------------------ #
    #                       Returning displacement vector                      #
    # ------------------------------------------------------------------------ #

    return u

def newmarkB_linAcc(pt, t, delta_t, m, c, k, u_0, dudt_0):
    '''
    gamma = 1/2; beta=1/6
    INPUT:
        - pt      : an array giving the discretized load p(t) (in the case of an 
                    earthquake base excitation pt = -m*acc(t))
        - t       : time points for the computation of u(t)
        - delta_t : the time step used
        - m       : Mass of the system
        - c       : Damping coefficient of the system
        - k       : Elastic stiffness of the system
        - u_0     : initial displacement
        - dudt_0  : initial velocity
    OUTPUT:
        - u       : The computed displacement with time
    '''

    # ------------------------------------------------------------------------ #
    #                            Initial conditions                            #
    # ------------------------------------------------------------------------ #
    # Constants for the Newmark Beta method constant acceleration
    gamma = 1/2
    beta = 1/6

    # Vectors for storing the response
    u      = np.zeros_like(pt)
    dudt   = np.zeros_like(pt)
    d2udt2 = np.zeros_like(pt)

    # Initial computations
    d2udt2_0 = (1/m)*(pt[0] -c*dudt_0 - k*u_0)
    k_bar = k + m/(beta*delta_t**2) + c*gamma/(beta*delta_t)
    a = c*gamma/beta + m/(beta*delta_t)
    b = m/(2*beta) + c*delta_t*(gamma/(2*beta) - 1)

    # Initial values
    t[0]      = 0
    u[0]      = u_0
    dudt[0]   = dudt_0
    d2udt2[0] = d2udt2_0

    # ------------------------------------------------------------------------ #
    #                        For loop for each time step                       #
    # ------------------------------------------------------------------------ #

    u_i      = u[0]
    dudt_i   = dudt[0]
    d2udt2_i = d2udt2[0]

    for i in range(1, pt.size):
        delta_p_i = pt[i] - pt[i - 1]
        delta_p_ibar = delta_p_i + a*dudt_i + b*d2udt2_i
        delta_u_i = delta_p_ibar/k_bar
        delta_dudt_i = ((gamma/(beta*delta_t))*(delta_u_i-dudt_i*delta_t) + 
                     (1-gamma/(2*beta))*d2udt2_i*delta_t)
        delta_d2udt2_i = ((1/(beta*delta_t**2))*(delta_u_i - dudt_i*delta_t) - 
                          (1/(2*beta))*d2udt2_i)
        
        # Storing values for the iteration i
        t[i]      = t[i - 1] + delta_t
        u[i]      = u[i - 1] + delta_u_i
        dudt[i]   = dudt[i - 1] + delta_dudt_i
        d2udt2[i] = d2udt2[i - 1] + delta_d2udt2_i

        # New values for the next iteration
        u_i = u[i]
        dudt_i = dudt[i]
        d2udt2_i = d2udt2[i]
    
    # ------------------------------------------------------------------------ #
    #                       Returning displacement vector                      #
    # ------------------------------------------------------------------------ #

    return u
    

def pseudo_SA(gm_rcrd, dt, periods, xi):
    '''
    INPUT:
        - gm_rcrd: ground-motion record, in GRAVITY (G) units
        - periods: periods for the computation of the pSA
        - xi     : damping coefficient
    OUTPUT:
        - pSA    : pseudo-spectral acceleration (GRAVITY)
    NOTES: 
        - USE GRAVITY UNITS for the ground-motion acceleration
        - This function uses the Newmark-Beta methods with constant acceleration
          (gamma=1/2, beta=1/4)
    '''
    m = 1
    pt = -m*gm_rcrd
    t = np.zeros_like(gm_rcrd)
    
    pSA = np.zeros_like(periods)

    for i in range(len(pSA)):
        wn = 2*np.pi/periods[i]
        k = m*wn**2
        c = 2*m*wn*xi
        u = newmarkB_constAcc(pt=pt, t=t, delta_t=dt, m=m, c=c, k=k, u_0=0, 
                              dudt_0=0)
        pSA[i] = np.max(np.abs(u))*(wn)**2
    
    return pSA


# ------------------------- End of callable functions ------------------------ #

if __name__=='__main__':

    filePath = './sample_rcrds'
    fileName = 'RSN808_LOMAP_TRI000.AT2' #gm in gravity

    gm_rcrd, gm_npts, gm_dt = gm_formatSeries.read_NGAWest2(filePath, fileName)

    xi = 0.05
    periods = np.linspace(0.01, 10, 1000)
    pSA = pseudo_SA(gm_rcrd, gm_dt, periods, xi)

    plt.plot(periods, pSA)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()