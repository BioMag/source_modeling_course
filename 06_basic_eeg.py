#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MNE - basic operations on EEG file - segmetation/averaging
"""


#%% Cell #0
""" Load the data
"""
import mne
INP_FNAME = '~/scratch/Flankers_mark_bad_filt.fif'
raw_filtered = mne.io.Raw(INP_FNAME, preload=True)


#%% Cell #1
""" Events and annotations are different animals in MNE, so we need to convert
    between the two.
"""
events, event_dict = mne.events_from_annotations(raw_filtered)

""" Take a quick look at the events, event_dict. Note that 'BAD_drift' annotation has not
    been converted to an event.
"""


#%% Cell #2
""" Segment the data
"""
# Note 'reject_by_annotation=True'. We dont want segments from the 'BAD_drift'
# part of the data.
epochs = mne.Epochs(raw_filtered, events, tmin=-0.3, tmax=0.7, event_id=event_dict, reject_by_annotation=True)

""" We can look at the segmented data same way as we look at the raw one - by
    using .plot()
"""
epochs.plot()

""" As with many other objects in MNE, we can also get a quick overview of the
    epochs by printing it (or just typing it's name in the console)
"""
print(epochs)


#%% Cell #3
""" We can select the relevant events by indexing epoch with the event name
    pattern
"""
s_epochs = epochs['stimulus']
sctl_epochs = epochs['stimulus/compatible/target_left']

print(epochs)       # All the epochs
print('\n')
print(s_epochs)     # All the epochs of type 'stimulus/...'
print('\n')
print(sctl_epochs)  # Only the 'stimulus/compatible/target_left' epochs


#%% Cell #4
""" Note that we can delete events by clicking the traces (unlike with the raw
    data, they are deleted, not just marked) ... 
"""
print(sctl_epochs)
sctl_epochs.plot()  # Delete some epochs here


#%% Cell #5
""" ... and verify that the clicked epochs were deleted
"""
print('\n')
print(sctl_epochs)


#%% Cell #6
""" Finally, let's average all the 'stimulus/...' epochs and look at the ERPs
"""
evoked = s_epochs.average()
evoked.plot()   # Note that the bad channels are excluded