import numpy as np
from scipy.integrate import cumtrapz

def conv_M02Mw():
    
    return None

def g_2_cms2(gm_record):
    # Converts units of a ground-motion record -> Gravity to cm/s2
    gm_cms2 = gm_record*981
    return gm_cms2

def cms2_2_g(gm_record):
    # Converts units of a ground-motion rec ord -> cm/s2 to gravity
    gm_gravity = gm_record/981
    return gm_gravity

def intgGM(gm_record, dt):
    # Integrates a ground-motion record
    # Assumes the initial values is 0
    gmInt = cumtrapz(gm_record, dx=dt, initial=0)
    return gmInt

def diffGM(gm_record, dt):
    # Differentiates a ground-motion record
    gmDiff = np.gradient(gm_record, dt)