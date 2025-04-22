r"""FILE TITLE

PURPOSE: 
# ------------------------------------- . ------------------------------------ #
FUNCTIONS:
funct1    : short description
# ------------------------------------- . ------------------------------------ #
AUTHORSHIP
Written by: Juan Jose Sepulveda Garcia
Mail      : jjs134@uclive.ac.nz / jjsepulvedag@unal.edu.co
Date      : March 2025
# ------------------------------------- . ------------------------------------ #
REFERENCES:
NA

IMPORTANT NOTES
Most of these functions require the IMs function as an argument. For most IMs 
this is easy. However, for other IMS (such as pSA) we have to use either 
partial functions (from functools import partial) or lambda function to set 
the parameters inside the IM function and only let the waveform varying. 
"""

import numpy as np

def rotateGM(gm000, gm090, theta):

    gm_r = gm000*np.cos(theta) + gm090*np.sin(theta) # rotated ground motion

    return gm_r



def rotD50(gm000, gm090, N, imFunc, nIM):
    '''
    INPUT: 
        - gm000: ground-motion record, component 000 (north) 
        - gm090: ground-motion record, component 090 (east) 
        - N: number of elements for the computation of rotd50 (rotations)
        - imFunc: intensity-measure function
        - nIm: number of elements returned by inFunc. For most IMs, this value 
        is equal to 1, for pSA this value depends on the number of periods
    NOTE: 
        PLEASE INCLUDE A N EQUAL OR GREATER THAN 2. 
        - For a dStep of 01°, use N=181
        - For a dStep of 02°, use N=91
        - For a dStep of 05°, use N=37 
        - For a dStep of 10°, use N=19
        - For a dStep of 15°, use N=13
        - For a dStep of 20°, use N=10
        - For a dStep of 30°, use N=07
        - For a dStep of 45°, use N=05
    '''

    thetas = np.radians(np.linspace(0, 180, N))
    ims = np.zeros((thetas.shape[0], nIM))

    for i in range(thetas.shape[0]):
        gm_r = rotateGM(gm000, gm090, thetas[i]) # get rotated ground motion
        ims[i, :] = imFunc(gm_r)
    
    imRotd50 = np.median(ims, axis=0) 
    
    return imRotd50

def rotD100():

    return None

def geoMean(gm000, gm090, imFunc):
    im000 = imFunc(gm000)
    im090 = imFunc(gm090)
    imGM = np.sqrt(im000*im090)
    return imGM

def average(gm000, gm090, imFunc):
    im000 = imFunc(gm000)
    im090 = imFunc(gm090)
    imMean = np.sqrt(im000*im090)
    return imMean

