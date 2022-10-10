# -*- coding: utf-8 -*-
"""

Create epochs and evoked responses from your raw data


"""

import mne
import os
import numpy as np

# from settings_sample import (bandpass_fmin, 
#                              bandpass_fmax, 
#                              event_ids,  
#                              epoch_tmin, 
#                              epoch_tmax, 
#                              reject,
#                              baseline)


# Subject
SUBJECT = 'sample'
# Task
TASK = 'audvis'


DATA_PATH = '/projects/BioMag_pipelines/MNE-sample-data/MEG/sample/'
OUTPUT_PATH = '/home/mialilj/source-localization-course' 

RAW_FNAME = 'sample_audvis_raw.fif'

#RAW_FNAME = f'{subject}_{task}_raw.fif'


raw = mne.io.read_raw_fif(os.path.join(DATA_PATH,RAW_FNAME), preload = True)
raw.load_data()


# #################################################
# # Remove artefacts, currently using PCA!!!!! You will probably want to change this to ICA (set ica to True)

# projs_ecg, _ = mne.preprocessing.compute_proj_ecg(raw, n_grad=2, n_mag=2)
# projs_eog, _ = mne.preprocessing.compute_proj_eog(raw, n_grad=2, n_mag=2)
    
# raw.info['projs'] += projs_ecg
# raw.info['projs'] += projs_eog
# raw.apply_proj()
# #################################################

# Experimental conditions
CONDITIONS = ["aud_l", "aud_r", "vis_l", "vis_r"]
# Event ids
EVENT_IDS = {"auditory/left":1, "auditory/right":2, "visual/left":3, "visual/right":4, "smiley":5, "buttonpress":32} 
# Time window (relative to stimulus onset)
epoch_tmin, epoch_tmax = -0.2, 0.5
# Baseline window
baseline = (-0.2,0)
# Filter settings
bandpass_fmin, bandpass_fmax = None, 40
# Rejection limits
reject = dict(grad=4000e-13, mag=4e-12, eog=150e-6)  


# Filter
raw.filter(bandpass_fmin, 
           bandpass_fmax) # check default filtering

# Get epochs and average
events =  mne.find_events(raw, 
                          min_duration = 2/raw.info['sfreq'])

epochs = mne.Epochs(raw, 
                    events, 
                    EVENT_IDS, 
                    epoch_tmin, 
                    epoch_tmax, 
                    baseline = baseline, 
                    preload=True, 
                    reject=reject, 
                    proj=False) 


# Apply precomputed ICA

# ica= mne.preprocessing.read_ica(fname.ica(subject=subject, method='infomax', ses=ses, task=task))
# ica.apply(epochs, exclude=ica.exclude)


# Save epochs   
epochs.save(fname.epochs(subject=subject,ses=ses,task=task),overwrite=True)
   
  
# Calculate and save evoked responses

    
evokeds=list()
for cond in conditions:
    evoked = epochs[cond].average()
    evokeds.append(evoked)

# Save evoked responses 
mne.write_evokeds(fname.evoked(subject=subject,ses=ses,task=task),evokeds)

