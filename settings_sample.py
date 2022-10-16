"""
===========
Config file
===========

Configuration parameters for the sample dataset.
"""

# Task
task = 'audvis'
# Sessions
sessions = ['01','02']
# Runs
runs = ['01','02'] 
# Experimental conditions
conditions = ["aud_l", "aud_r", "vis_l", "vis_r"]
# Event ids
event_ids = {"auditory/left":1, "auditory/right":2, "visual/left":3, "visual/right":4, "smiley":5, "buttonpress":32} 
# Time window (relative to stimulus onset)
epoch_tmin, epoch_tmax = -0.2, 0.5
# Baseline window
baseline = (-0.2,0)
# Filter settings
bandpass_fmin, bandpass_fmax = None, 40
# ICA method
ica_method='infomax'
# Rejection limits
reject = dict(grad=4000e-13, mag=4e-12, eog=150e-6)  