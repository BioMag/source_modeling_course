#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MNE - basic operations on EEG file - filtering
"""

#%% Cell #0
""" Load the data
"""
import mne
INP_FNAME = '~/scratch/Flankers_mark_bad.fif'
raw_data_obj = mne.io.Raw(INP_FNAME, preload=True)


#%% Cell #1
""" Do the high-pass filtering to remove the drift
"""
CUTOFF_FREQ = 0 # Hz, what frequency we should use?
raw_filtered = raw_data_obj.copy()      # The filtering is done in-place
raw_filtered.filter(l_freq=CUTOFF_FREQ, h_freq=None)

raw_filtered.plot()

""" Check that the filtering fixed the drift
"""


#%% Cell #2
""" Save the filtered data
"""
OUT_FNAME = '~/scratch/Flankers_mark_bad_filt.fif'
raw_filtered.save(OUT_FNAME)