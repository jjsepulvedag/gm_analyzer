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
import gm_formatSeries

def PGA(accs):
    '''
    INPUT
        accs: ground-motion acceleration
    OUTPUT: 
        PGA:  peak ground acceleration
    '''
    PGA = np.max(np.abs(accs))
    return PGA

def PGV(vels):
    '''
    INPUT
        vels: ground-motion velocities
    OUTPUT: 
        PGV:  peak ground velocity
    '''
    PGV = np.max(np.abs(vels))
    return PGV

def PGD(disp):
    '''
    INPUT
        disp: ground-motion displacements
    OUTPUT: 
        PGD:  peak ground displacement
    '''
    PGD = np.max(np.abs(disp))

    return PGD

# ------------------------- End of callable functions ------------------------ #

if __name__=='__main__':

    filePath = './sample_rcrds'
    fileAcc = 'RSN808_LOMAP_TRI000.AT2'
    fileVel = 'RSN808_LOMAP_TRI000.VT2'
    fileDis = 'RSN808_LOMAP_TRI000.DT2'

    gm_acc, gm_npts, gm_dt = gm_formatSeries.read_NGAWest2(filePath, fileAcc)
    gm_vel, gm_npts, gm_dt = gm_formatSeries.read_NGAWest2(filePath, fileVel)
    gm_dis, gm_npts, gm_dt = gm_formatSeries.read_NGAWest2(filePath, fileDis)

    pga = PGA(gm_acc)
    pgv = PGV(gm_vel)
    pgd = PGD(gm_dis)

    print('PGA: {0}, PGV: {1}, PGD:{2}'.format(pga, pgv, pgd))

