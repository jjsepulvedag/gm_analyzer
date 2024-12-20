"""
--------------------------------------------------------------------------------
PURPOSE:
Computation of the Fourier Amplitude Spectrum of a ground motion
--------------------------------------------------------------------------------
FUNCTIONS:
    - fft: computes fast fourier transform for real input (np.rfft)
    - FAS: computes Fourier Amplitude Spectrum
--------------------------------------------------------------------------------
NOTES:
    - fast fourier transform computed used np.rfft, which is basically the 
    computation of the fft for real input
--------------------------------------------------------------------------------
REFERENCES:
    - Baker, J., Bradley, B., & Stafford, P. (2021). Seismic hazard and risk 
    analysis. Cambridge University Press.
"""

import numpy as np
import gm_formatSeries
import matplotlib.pyplot as plt

def fft(y, dt, n):
    '''
    INPUT: 
        - y : waveform
        - dt: time step
        - n : number of points
    OUTPUT:
        - fa_spectrum : Fourier Amplitude Spectrum 
        - fa_freq     : frequencies of the Fourier Amplitude Spectrum
    '''
    nfft = 2 ** int(np.ceil(np.log2(n)))
    fa_spectrum = np.fft.rfft(y, n=nfft, axis=0) 
    fa_freq = np.fft.rfftfreq(nfft, dt)
    
    return fa_spectrum, fa_freq


def FAS(gmSeries, dt):
    '''
    INPUT:
        - gmSeries: ground motion series
        - dt: time step of the series
    OUTPUT:
        - fas: fourier amplitude spectrum
        - faf: fourier amplitude frequencies
    '''
    fas, faf = fft(gmSeries, dt, gmSeries.shape[0])
    
    return fas, faf

def smooth_FAS(fas, ffeq, method):

    if method == 'KO98':
        # see page 154 Brendon textbook
        continue
    elif method == 'BooreXX'
        continue
    else:
        print('method not found')

    return None


if __name__=='__main__':

    filePath = './sample_rcrds'
    file_TI = 'RSN808_LOMAP_TRI000.AT2' #gm in gravity
    file_YB = 'RSN813_LOMAP_YBI000.AT2' #gm in gravity

    gm_rcrdTI, gm_nptsTI, gm_dtTI = gm_formatSeries.read_NGAWest2(filePath, 
                                                                  file_TI)
    gm_rcrdYB, gm_nptsYB, gm_dtYB = gm_formatSeries.read_NGAWest2(filePath, 
                                                                  file_YB)

    fa_sptrmTI, fa_freqsTI = FAS(gm_rcrdTI, gm_dtTI)
    fa_sptrmTI = np.abs(fa_sptrmTI)
    fa_sptrmYB, fa_freqsYB = FAS(gm_rcrdYB, gm_dtYB)
    fa_sptrmYB = np.abs(fa_sptrmYB)

    plt.plot(fa_freqsTI, fa_sptrmTI)
    plt.plot(fa_freqsYB, fa_sptrmYB)
    plt.xlim(0.02, 50)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()