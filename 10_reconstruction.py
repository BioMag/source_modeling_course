#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solving the inverse problem
"""

#%% Cell #0
""" Load things
"""
import mne
FWD_FNAME = mne.get_config('SCRATCH_DIR') + '/sample_audvis_raw-fwd.fif'
RAW_FNAME = mne.get_config('DATA_DIR') + '/MEG/sample_audvis_raw.fif'

fwd = mne.read_forward_solution(FWD_FNAME)
raw = mne.io.Raw(RAW_FNAME, preload=True)

event_dict = {'auditory/left': 1, 'auditory/right': 2, 'visual/left': 3,
              'visual/right': 4, 'face': 5, 'buttonpress': 32}


#%% Cell #1
""" Create an epoch file and prepare the covarience matrix
"""
picks = mne.pick_types(raw.info, meg=True, eeg=False, eog=True, exclude='bads')

events = mne.find_events(raw)
epochs = mne.Epochs(raw,
                    events,
                    event_id=event_dict,
                    tmin=-0.2, tmax=0.5,
                    proj=True,
                    picks=picks,
                    baseline=(None, 0),
                    preload=True,
                    reject=dict(grad=4000e-13, mag=4e-12, eog=150e-6))

cov = mne.compute_covariance (epochs, tmax=0)


#%% Cell #2
""" Compute the inverse solution
"""
inv = mne.minimum_norm.make_inverse_operator(raw.info, fwd, cov, loose=0.2)


#%% Cell #3
""" Apply the inverse solution
"""
evoked = epochs['visual/right'].average()
stc = mne.minimum_norm.apply_inverse(evoked, inv, lambda2=1./9., method='dSPM')


#%% Cell #4
""" Plot the inverse solution
"""
stc.plot(hemi='both')


#%% Cell #5
""" Morph to average and plot
"""
stc_fs = mne.compute_source_morph(stc, 'sample', 'fsaverage', smooth=5, verbose='error').apply(stc)
stc_fs.plot(hemi='both') # try also surface='flat'


#%% Cell #6
""" Access the source data directly
"""
import matplotlib.pylab as plt
print(stc.data.shape)
print(stc.rh_data.shape)

plt.plot(stc.lh_data[0,:])
plt.plot(stc.rh_data[0,:])
