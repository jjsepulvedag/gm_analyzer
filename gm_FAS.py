import numpy as np

def fft(y, dt, n):
    nfft = 2 ** int(np.ceil(np.log2(n)))
    fa_spectrum = np.fft.rfft(y, n=nfft, axis=0) * dt
    fa_freq = np.fft.rfftfreq(nfft, dt)
    return fa_spectrum, fa_freq


def FAS(gmSeries, dt):
    '''
    fas: fourier amplitude spectrum
    faf: fourier amplitude frequencies
    '''
    fas, faf = fft(gmSeries, dt, gmSeries.shape[0])
    return fas, faf

# def invFAS(fas, faf, dt):
#     '''
#     fas: fourier amplitude spectrum
#     faf: fourier amplitude frequencies
#     '''
