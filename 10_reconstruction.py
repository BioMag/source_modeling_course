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


#%% Cell #1
""" reconstruction
"""

# extract epochs and save them
picks = mne.pick_types(raw.info, meg=True, eeg=False, eog=True, exclude='bads')

events = mne.find_events(raw)
epochs = mne.Epochs(raw,
                    events,
                    event_id=1,
                    tmin=-0.2, tmax=0.5,
                    proj=True,
                    picks=picks,
                    baseline=(None, 0),
                    preload=True,
                    reject=dict(grad=4000e-13, mag=4e-12, eog=150e-6))
# compute evoked response and noise covariance,and plot evoked
evoked = epochs.average ()
cov = mne.compute_covariance (epochs, tmax=0)


inv = mne.minimum_norm.make_inverse_operator(raw.info, fwd, cov, loose=0.2)
# compute inverse solution
stc = mne.minimum_norm.apply_inverse(evoked, inv, lambda2=1./9., method='dSPM')

stc.plot()