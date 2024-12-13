"""
--------------------------------------------------------------------------------
PURPOSE:
Computation of peak ground acceleration/velocity/displacement of an earthquake
ground motion.
--------------------------------------------------------------------------------
FUNCTIONS:
    - PGA(): computes (returns) peak ground acceleration
    - PGV(): computes (returns) peak ground velocity
    - PGD(): computes (returns) peak ground displacement
--------------------------------------------------------------------------------
NOTES:

--------------------------------------------------------------------------------
REFERENCES:
    - Kramer, S. L., & Stewart, J. P. (2024). Geotechnical earthquake 
    engineering. CRC Press.
    - Baker, J., Bradley, B., & Stafford, P. (2021). Seismic hazard and risk 
    analysis. Cambridge University Press.
"""

import numpy as np

def PGA(accs):
    '''
    INPUT
        accs: ground-motion acceleration
        dt  : delta of time
    OUTPUT: 
        PGA:  peak ground acceleration
    '''
    PGA = np.max(np.abs(accs))
    return PGA

def PGV(vels):
    '''
    INPUT
        vels: ground-motion velocities
        dt  : delta of time
    OUTPUT: 
        PGV:  peak ground velocity
    '''
    PGV = np.max(np.abs(vels))
    return PGV

def PGD(disp):
    '''
    INPUT
        disp: ground-motion displacements
        dt  : delta of time
    OUTPUT: 
        PGD:  peak ground displacement
    '''
    PGD = np.max(np.abs(disp))

    return PGD

if __name__=='__main__':
    print('Hello World!')


