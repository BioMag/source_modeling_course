#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Forward modeling
"""


#%% Cell #0
""" First, we need to coregister MRI and MEG. Save the coregistration to the
    sample_audvis_raw-trans.fif in the scratch folder.
"""
import mne
mne.gui.coregistration()


#%% Cell #1
""" Create the source space
"""
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


#%% Cell #3
""" BEM-related computations
"""
CONDUCTIVITY = (0.3,)   # for a single layer, for three layers use
                        # (0.3, 0.006, 0.3)
model = mne.make_bem_model(subject='sample', ico=4, conductivity=CONDUCTIVITY)
bem = mne.make_bem_solution(model)


#%% Cell #4
""" Compute the forward solution ...
"""
TRANS_FNAME = mne.get_config('SCRATCH_DIR') + '/sample_audvis_raw-trans.fif'
RAW_FNAME = mne.get_config('DATA_DIR') + '/MEG/sample_audvis_raw.fif'

fwd = mne.make_forward_solution(RAW_FNAME, trans=TRANS_FNAME, src=src, bem=bem,
                                meg=True, eeg=False, mindist=5.0, n_jobs=1,
                                verbose=True)


#%% Cell #5
""" ... and write it to the disk
"""
FNAME = mne.get_config('SCRATCH_DIR') + '/sample_audvis_raw-fwd.fif'
mne.write_forward_solution(FNAME, fwd)


