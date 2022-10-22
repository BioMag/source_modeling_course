#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The basics of MNE
"""

#%% Cell #0
""" MNE is Python package
"""
import mne              # Let's load MNE
print(mne.__version__)  # And check it's version


#%% Cell #1
""" Let's load some EEG data
"""
FNAME = '~/storage/Data/mne_data/MNE-ERP-CORE-data/ERP-CORE_Subject-001_Task-Flankers_eeg.fif'
raw_data_obj = mne.io.Raw(FNAME, preload=True)


#%% Cell #2
""" Let's also look at the data
"""
raw_data_obj.plot()


#%% Cell #3
""" Now, let's look at the file's info attribute
"""
print(raw_data_obj.info)
""" Explore raw_data_obj and raw_data_obj.info using spyder:
    1. Use TAB after . (e.g. type raw_data_obj. in the console and press TAB)
       to get available methods/attributes
    2. Explore variables in the variable explorer
    3. Use online help -- try using Ctrl-I on various things

    Can you figure out the subject's sex?
"""


#%% Cell #4
""" What about the actual numerical measurement data? Here's the
    straightforward way
"""
raw_data = raw_data_obj.get_data()  # raw_data is a numpy array
n_chan, n_samp = raw_data.shape    # note multiple assignment

print('We have %i channels of %i samples each' % (n_chan, n_samp))
""" Can you get the total duration of the recording in seconds?
"""
# t_tot = 


#%% Cell #5
""" Let's get the data for FC3 ...
"""
ch_names = raw_data_obj.info.ch_names
FC3_idx = ch_names.index('FC3')
FC3_data = raw_data[FC3_idx,:]


#%% Cell #6
""" ... and the corresponding time index ...
"""
import numpy as np
t = np.linspace(0, t_tot, n_samp)


#%% Cell #7
""" ... and plot the data
"""
import matplotlib.pylab as plt
plt.plot(t, FC3_data)
plt.show()

""" Any guesses about the units?
"""


#%% Cell #8
""" A cool pythonic way to do the same thing: indexing the raw_data_obj
    directly
"""
FC3_data, t = raw_data_obj['FC3', :]
plt.plot(t, FC3_data.T)     # Note the transpose!
                            # FC3_data is 1-by-n matrix, not n-dimensional vector
plt.show()

