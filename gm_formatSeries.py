import os
import numpy as np
import matplotlib.pyplot as plt

def read_NGAWest2(fileLoc, fileName):
    '''
    The web-based Pacific Earthquake Engineering Research Center (PEER) ground 
    motion database provides tools for searching, selecting and downloading 
    ground motion data. 
    NGA-West2 -- Shallow Crustal Earthquakes in Active Tectonic Regimes
    Website: ngawest2.berkeley.edu/
    '''

    with open("/".join([fileLoc, fileName]), 'r') as f:
        all_lines = f.readlines()

    gm_raw = []

    line0 = all_lines[3].split() 
    npts = int(line0[(line0.index('NPTS='))+1].rstrip(',')) 
    dt = float(line0[(line0.index('DT='))+1])

    for line_i in all_lines[4:]:
        gm_raw.append([float(numbr) for numbr in line_i.split()])

    gm_raw = np.concatenate(gm_raw)

    return gm_raw, npts, dt

def read_NGAEast(fileLoc, fileName):

    return None

def read_COSMOS(fileLoc, fileName):
    
    return None

def read_GP2010(loc, fname):
    """
    Convenience function for reading files in the Graves and Pitarka format
    INPUT:
        - loc: location of the ground-motion time series 
        - fname: file name
    OUTPUT:
        - data: ground-motion time series
        - num_pts: number of points of the waveform 
    """

    with open("/".join([loc, fname]), 'r') as f:
        lines = f.readlines()

    data = []

    for line in lines[2:]:
        data.append([float(val) for val in line.split()])

    data=np.concatenate(data)

    line1=lines[1].split()
    num_pts=float(line1[0])
    dt=float(line1[1])
    shift=float(line1[4])

    return data, num_pts, dt, shift




if __name__=='__main__':

    file_path = './sample_rcrds'
    file_name = 'RSN808_LOMAP_TRI000.AT2'

    gm_rcrd, npts, dt = NGA_West2(file_path, file_name)
    times = np.linspace(0, npts*dt, npts)
    
    plt.plot(times, gm_rcrd)
    plt.show()


