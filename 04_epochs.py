# -*- coding: utf-8 -*-
"""

Create epochs and evoked responses from your raw data


"""

import mne
import os
import numpy as np

from settings_sample import (bandpass_fmin, bandpass_fmax, runs, event_ids,  epoch_tmin, epoch_tmax, conditions, baseline)


subject = 'sample'
ses = '01'
task = 'audvis'
run = '01'
proc = 'raw'


raw = mne.io.read_raw_fif(fname.raw(subject=subject,
                                    ses=ses,
                                    task=task,
                                    run=run,
                                    proc=proc, 
                                    preload = True))
raw.load_data()



#################################################
# Remove artefacts, currently using PCA!!!!! You will probably want to change this to ICA (set ica to True)
if ica==False:
    projs_ecg, _ = mne.preprocessing.compute_proj_ecg(raw, n_grad=2, n_mag=2)
    projs_eog, _ = mne.preprocessing.compute_proj_eog(raw, n_grad=2, n_mag=2)
        
    raw.info['projs'] += projs_ecg
    raw.info['projs'] += projs_eog
    raw.apply_proj()
#################################################

# Filter
raw.filter(bandpass_fmin, bandpass_fmax) # check default filtering
raw.notch_filter(freqs=np.arange(50, 251, 50))

# Get epochs and average
events =  mne.find_events(raw, min_duration = 2/raw.info['sfreq'])
epochs = mne.Epochs(raw, events, event_ids, epoch_tmin, epoch_tmax, baseline = baseline, 
                    preload=True, reject=reject, proj=False) 


# Apply precomputed ICA
if ica==True:
    ica= mne.preprocessing.read_ica(fname.ica(subject=subject, method='infomax', ses=ses, task=task))

    ica.apply(epochs, exclude=ica.exclude)

# Save epochs
if not os.path.exists(fname.megprocessed_dir(subject=subject, ses=ses) + 'epochs/'):    
    os.makedirs(fname.megprocessed_dir(subject=subject,ses=ses) + 'epochs/')
epochs.save(fname.epochs(subject=subject,ses=ses,task=task),overwrite=True)
     
# Calculate and save evoked responses
if not os.path.exists(fname.megprocessed_dir(subject=subject, ses=ses) + 'evoked/'):    
    os.makedirs(fname.megprocessed_dir(subject=subject,ses=ses) + 'evoked/')
    
evokeds=list()
for cond in conditions:
    evoked = epochs[cond].average()
    evokeds.append(evoked)

# Save evoked responses 
mne.write_evokeds(fname.evoked(subject=subject,ses=ses,task=task),evokeds)

