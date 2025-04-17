"""
--------------------------------------------------------------------------------
PURPOSE:
Computing significant ground-motion duration (D_575, D595)
--------------------------------------------------------------------------------
FUNCTIONS:
    - D_575: computes the 5-75% significant duration
    - D_595: computes the 5-95% significant duration
--------------------------------------------------------------------------------
NOTES:
    - The energy contained in a ground-motion time series is proportional to the 
    cumulative squared acceleration. For this reason, I call the AI function 
    for the computation of the significant durations
--------------------------------------------------------------------------------
REFERENCES:
    - Baker, J., Bradley, B., & Stafford, P. (2021). Seismic hazard and risk 
    analysis. Cambridge University Press.
"""

import numpy as np
from gm_analyzer import gm_CIMs, gm_formatSeries
# import gm_CIMs
# import gm_formatSeries


def D_575(gm_rcrd, dt):
    '''
    INPUT:
        - gm_rcrd : ground-motion acceleration record
        - dt      : time step
    OUTPUT:
        - D_575   : 5-75% significant duration
    '''
    arias_intesity = gm_CIMs.vAI(gm_rcrd, dt)
    normalized_AI = arias_intesity/np.max(arias_intesity)

    idx_d5 = np.argmin(np.abs(normalized_AI-0.05))
    idx_d75 = np.argmin(np.abs(normalized_AI-0.75))

    D_575 = (idx_d75 - idx_d5)*dt

    return D_575


def D_595(gm_rcrd, dt):
    '''
    INPUT:
        - gm_rcrd : ground-motion acceleration record
        - dt      : time step
    OUTPUT:
        - D_595   : 5-95% significant duration
    '''
    arias_intesity = gm_CIMs.vAI(gm_rcrd, dt)
    normalized_AI = arias_intesity/np.max(arias_intesity)

    idx_d5 = np.argmin(np.abs(normalized_AI-0.05))
    idx_d95 = np.argmin(np.abs(normalized_AI-0.95))

    D_595 = (idx_d95 - idx_d5)*dt

    return D_595


if __name__=='__main__':

    filePath = './sample_rcrds'
    file_TI = 'RSN808_LOMAP_TRI000.AT2' #gm in gravity
    file_YB = 'RSN813_LOMAP_YBI000.AT2' #gm in gravity

    gm_rcrdTI, gm_nptsTI, gm_dtTI = gm_formatSeries.read_NGAWest2(filePath, 
                                                                  file_TI)
    gm_rcrdYB, gm_nptsYB, gm_dtYB = gm_formatSeries.read_NGAWest2(filePath, 
                                                                  file_YB)


    d575_TI = D_575(gm_rcrdTI, gm_dtTI)
    d595_TI = D_595(gm_rcrdTI, gm_dtTI)
    print('Treasure Island Duration, D575: {}s, D595: {}s'.format(d575_TI, 
                                                                  d595_TI))

    d575_YB = D_575(gm_rcrdYB, gm_dtYB)
    d595_YB = D_595(gm_rcrdYB, gm_dtYB)
    print('Yerba Buena Duration, D575: {}s, D595: {}s'.format(d575_YB, 
                                                              d595_YB))
