#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MNE - basic operations on EEG file - data review/cleaning
"""

#%% Cell #0
""" Load the data
"""
import mne
FNAME = '~/source_modeling_course/data/EEG/Flankers.fif'
raw_data_obj = mne.io.Raw(FNAME, preload=True)


#%%
""" Let's look at the data a bit more in depth
"""


#%% Cell #1
"""  Plot spectra
"""
import numpy as np
raw_data_obj.plot_psd(tmax=np.inf, fmax=80, average=False)

#%% Cell #2
""" Let's try different spectral resolutions
"""
raw_data_obj.plot_psd(tmax=np.inf, fmax=80, average=False, n_fft=128)
raw_data_obj.plot_psd(tmax=np.inf, fmax=80, average=False, n_fft=1024)


#%% Cell #3
"""  Eyeball the raw data.
"""
raw_data_obj.plot()

""" Go through the data channel-by-channel. Can you you see any issues?
"""


#%% Cell #4 - run outside of Spyder!
""" Let's fix the problem by manually marking bad channels and segments.
    Unfortunately, because of a Spyder bug, we'll have to use something else
    to run this code.
"""
import mne
INP_FNAME = '~/source_modeling_course/data/EEG/Flankers.fif'

raw_data_obj = mne.io.Raw(INP_FNAME, preload=True)
raw_data_obj.plot()


#%% Cell #5 - run outside of Spyder!
""" Check that the raw_data_obj has been updated. Any ideas how?
"""


#%% Cell #6 - run outside of Spyder!
""" Save the modified file 
"""
# Append the '_marked_bad' to the previous file name
OUT_FNAME = '~/scratch/Flankers_mark_bad.fif'
raw_data_obj.save(OUT_FNAME)

""" Check that the file has been created
"""
