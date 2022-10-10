#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:45:44 2019

Simple example for how to use mne_bids to save your data in BIDS format

Change according to your needs

@author: mhusberg
"""

import os.path as op
import mne

from mne_bids import (write_raw_bids, BIDSPath, print_dir_tree)

from config import study_path

# Sample subject
subject_in = 'sample'

# Rawdata folder
data_path = op.join(study_path, 'MEG')

# Output file
output_path = op.join(study_path, 'BIDS')
subject_out = '01' # subject-id: '01' -> 'sub-01' in BIDS structure

# Define event IDs according to your project
#events = {'Category1':1, 'Category2': 2, 'Other event': 3}

# For the sample data:
events = {"auditory/left":1, "auditory/right":2, "visual/left":3, "visual/right":4, "smiley":5, "buttonpress":32} 

def create_BIDS(filename, subject_in, subject_out, session, run, proc, task, event_id): # add date if necessary

    # Read in data
    raw_fname = op.join(data_path, subject_in, filename) # Folder structure for recorded raw data
    #raw_fname = op.join(data_path, 'MEG', subject_in, date, filename) # Add date if necessary
    raw = mne.io.read_raw_fif(raw_fname)
    events_data = mne.find_events(raw, min_duration=2/1000.)

    bids_path = BIDSPath(subject=subject_out, 
                         session=session, 
                         task=task, 
                         run=run, 
                         processing=proc, 
                         root=output_path)
    
    write_raw_bids(raw, 
                   bids_path, 
                   events_data=events_data,
                   event_id=event_id, 
                   overwrite=True)

    print_dir_tree(output_path)


#######################################################################
# Session 1
#date = 'YYMMDD' # date when measured, if in folder structure
session = '01'
proc = 'raw' 

###########
# Task: audvis
task = 'audvis'

# Filename, run 1
filename='sample_audvis_run01_ses01_raw.fif' # Fill in name of rawdata-file 1
run = '01'

create_BIDS(filename, subject_in, subject_out, session, run, proc, task, events) # add date if necessary

# Filename, run 2
filename='sample_audvis_run02_ses01_raw.fif' # Fill in name of rawdata-file 2
run = '02'

create_BIDS(filename, subject_in, subject_out, session, run, proc, task, events) # add date if necessary


