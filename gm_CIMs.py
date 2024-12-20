import numpy as np
import gm_formatSeries
import matplotlib.pyplot as plt

def AI(gm_rcrd, dt):
    '''
    INPUT:
        - gm_rcrd : ground-otion acceleration record (gravity)
        - dt      : time step
    OUTPUT:
        - arias_intensity: 
    '''
    grvt = 9.81
    gm2 = gm_rcrd**2

    constnt=np.pi/(2*grvt)
    arias_intensity = np.zeros_like(gm_rcrd)

    arias_intensity[0] = gm2[0]*dt
    for i in range(1, arias_intensity.shape[0]):
        arias_intensity[i] = constnt*(gm2[i]*dt) + arias_intensity[i-1]

    return arias_intensity

def CAV(gm_rcrd, dt):
    '''
    INPUT:
        - 
    OUTPUT:
        - 
    '''
    gm_abs = np.abs(gm_rcrd)
    cumm_abs_vel = np.zeros_like(gm_abs)

    cumm_abs_vel[0] = gm_abs[0]*dt

    for i in range(1, cumm_abs_vel.shape[0]):
        cumm_abs_vel[i] = gm_abs[i]*dt + cumm_abs_vel[i-1]
    

    return cumm_abs_vel

if __name__=='__main__':

    filePath = './sample_rcrds'
    file_TI = 'RSN808_LOMAP_TRI000.AT2' #gm in gravity
    file_YB = 'RSN813_LOMAP_YBI000.AT2' #gm in gravity

    gm_rcrdTI, gm_nptsTI, gm_dtTI = gm_formatSeries.read_NGAWest2(filePath, 
                                                                  file_TI)
    gm_rcrdYB, gm_nptsYB, gm_dtYB = gm_formatSeries.read_NGAWest2(filePath, 
                                                                  file_YB)

    gm_TI_AI = AI(gm_rcrdTI, gm_dtTI)
    gm_TI_CAV = CAV(gm_rcrdTI, gm_dtTI)
    time_TI = np.arange(0, gm_nptsTI*gm_dtTI, gm_dtTI)
    gm_YB_AI = AI(gm_rcrdYB, gm_dtYB)
    gm_YB_CAV = CAV(gm_rcrdYB, gm_dtYB)
    time_YB = np.arange(0, gm_nptsYB*gm_dtYB, gm_dtYB)

    plt.plot(time_TI, gm_TI_AI)
    plt.plot(time_YB, gm_YB_AI)
    plt.show()
    plt.plot(time_TI, gm_TI_CAV)
    plt.plot(time_YB, gm_YB_CAV)
    plt.show()