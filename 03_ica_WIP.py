# -*- coding: utf-8 -*-

import argparse
import mne
import os
import numpy as np

from config import (fname, session1, session2, proc,
                           default_baseline, reject, tasks, subjects, event_ids)

from settings_envspeech import (bandpass_fmin, bandpass_fmax, ica_epoch_tmin, ica_epoch_tmax)

###Work in progress

# Note: Automatic selection of ICA components does not work very well.
# Check every subject manually

# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject', help='The subject to process')
parser.add_argument('-ses', help='The session to process. ')
parser.add_argument('-method', help='Apply precomputed ICA')
args = parser.parse_args()
subject = args.subject
ses = args.ses
method = args.method

print('Processing subject: ', subject)
print('Processing session: ', ses)


# Do ICA on epochs or raw? How long epochs?

raws = list()
for run in runs:
    # Read the raw data
    raw = mne.io.read_raw_fif(fname.raw(subject=subject,
                                        ses=ses,
                                        task=task,
                                        run=run,
                                        proc=proc, 
                                        preload = False))
    raws.append(raw)

# Concatenate raw data, check that data has been transformed to the same position
raw=mne.concatenate_raws(raws)
events =  mne.find_events(raw, min_duration = 2/raw.info['sfreq'])

ch_names=raw.info['ch_names']

# Filter
raw.load_data()
raw.filter(1, None) # check default filtering
raw.notch_filter(freqs=np.arange(50, 251, 50))

# Get epochs and average
picks=mne.pick_types(raw.info, meg=True, eeg=False, emg=True, eog=True,
                               stim=False, misc=False, exclude='bads')
epochs = mne.Epochs(raw, events, event_ids, ica_epoch_tmin, ica_epoch_tmax, baseline = None, 
                    preload=True, reject=reject, proj=False, picks=picks) 

picks = mne.pick_types(raw.info)

# Save memory, delete raw
#del raw

def run_ica(method, raw_or_epochs, picks, n_components = 15, fit_params=None):

    ica = mne.preprocessing.ICA(n_components=n_components, method=method, fit_params=fit_params,
              random_state=97, max_iter=600)
    ica.fit(raw_or_epochs, picks=picks)
    
    return ica

def correlate_ica_with_emg(raw_or_epochs, ica, ch_name='EMG063', l_freq=1, h_freq=10, threshold=2):


    # find which ICs correlate with EMG    
    emg_indices, emg_scores = ica.find_bads_eog(raw_or_epochs, 
                                                ch_name=ch_name, 
                                                l_freq=l_freq, h_freq = h_freq, 
                                                threshold=threshold)
    #emg_scores = np.max(np.abs(emg_scores), axis=0)
    
    return emg_indices 

# Which ICA method? How many ICs? How mark correct ICs for exclusion?
# Works really poorly so far.    
# infomax on raw: best sofar, try before maxfiltering?

# Find ICs, use limited set of PCs
if method=='infomax':
    ica=run_ica('infomax', epochs, n_components=15, picks=picks, 
            fit_params=dict(extended=True))
if method=='fastica':
    ica=run_ica('fastica', epochs, n_components=15, picks=picks, 
            fit_params=None)
else:
    print('Raise error here: please specify valid ICA method')

# Correlate ICs with EMG
emg_indices=correlate_ica_with_emg(raw, ica, ch_name='EMG063', threshold=2)
# Correlate ICs with EOG
eog_indices=correlate_ica_with_emg(raw, ica, ch_name='EMG064', threshold=3)#FIXME:change to EOG channel
# Correlate ICs with virtual ECG channel
ecg_indices, ecg_scores = ica.find_bads_ecg(raw, method='ctps') # ECG artefact not found with 15 component infomax

# Mark ICs for exclusion
exclude_indices = emg_indices + eog_indices + ecg_indices
ica.exclude=exclude_indices

## Read template ICA solution: WIP
#ica_template = mne.preprocessing.read_ica(fname.ica(subject='ica_template', method='infomax', ses=ses, task=task))
#icas=[ica_template, ica] # template first, subject second
#eog_inds_template=1 # Visually checked from template
#corrmap_fig, labelled_ics=mne.preprocessing.corrmap(icas, template=(0, eog_inds_template),
#                                              ch_type='mag', label='eog', plot=True)


# Save ica solution
if not os.path.exists(fname.megprocessed_dir(subject=subject, ses=ses) + 'ica/'):    
    os.makedirs(fname.megprocessed_dir(subject=subject, ses=ses) + 'ica/')
ica.save(fname.ica(subject=subject, method='infomax', ses=ses, task=task))

#ica.apply(epochs, exclude=exclude_indices)
#plot figures and save

#Finally, IC epochs were averaged and correlated with a “speech template” 
#curve that was modelled as a sigmoidal curve with a slope starting at 200 ms 
#reaching a plateau at 1200 ms. ICs with a correlation of >0.8 were removed. 