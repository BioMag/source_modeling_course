#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Forward modeling
"""


#%% Cell #1
""" Create the source space
"""
import mne

src = mne.setup_source_space('sample', spacing='oct6', add_dist='patch')
mne.viz.plot_bem('sample', src=src)


#%% Cell #2
""" View all sources in 3d
"""
fig = mne.viz.plot_alignment(subject='sample',
                             surfaces='white',
                             coord_frame='mri',
                             src=src)
mne.viz.set_3d_view(fig, azimuth=173.78, elevation=101.75,
                    distance=0.30, focalpoint=(-0.03, -0.01, 0.03))

""" Do you think spacing 'oct6' would be better?
"""

#%% Cell #3
""" BEM-related computations
"""
CONDUCTIVITY = (0.3,)   # for a single layer, for three layers use
                        # (0.3, 0.006, 0.3)
model = mne.make_bem_model(subject='sample', ico=4, conductivity=CONDUCTIVITY)
bem = mne.make_bem_solution(model)


#%% Cell #4
""" Compute the leadfield
"""
import os

TRANS_FNAME = '%s/scratch/sample_audvis_raw-trans.fif' % os.getenv('HOME')
RAW_FNAME = '~/source_modeling_course/data/MEG/sample_audvis_raw.fif'

fwd = mne.make_forward_solution(RAW_FNAME, trans=TRANS_FNAME, src=src, bem=bem,
                                meg=True, eeg=False, mindist=5.0, n_jobs=1,
                                verbose=True)


#%% Cell #4
""" UNDER CONSTRUCTION
"""
raw = mne.io.Raw(RAW_FNAME, preload=True)

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