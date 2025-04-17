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


def rotD50(gm000, gm090, N, imFunc):
    '''
    Note: 
        Please include a N equal or greater than 2. For a dStep of 5°, use N=19
    '''

    theta = np.linspace(0, 90, N)

    



    return None

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

