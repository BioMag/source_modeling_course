#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:38:02 2021

Download example data for testing the pipeline

@author: mhusberg
"""
import os

import mne
from mne.datasets import sample

# Downloads the data (1.5GB) into mne_data, unless otherwise stated
data_path = sample.data_path(path='/projects/BioMag_pipelines', force_update=False)
subject = 'sample'
task = 'audvis'

# Read data
raw_fname = os.path.join(data_path, 'MEG', 'sample',
                                    'sample_audvis_raw.fif')
raw = mne.io.read_raw_fif(raw_fname)

# Cut data into 'runs' and 'sessions' for illustration purposes

# Run 01, Session 01
raw_snippet = raw.copy().crop(0, 60)
run = '01'
session = '01'
raw_fname = os.path.join(data_path, 'MEG', 'sample',
                                    'sample_audvis_run{}_ses{}_raw.fif'.format(run, session))
raw_snippet.save(raw_fname, overwrite=True)

# Run 02, Session 01
raw_snippet = raw.copy().crop(60, 120)  
run = '02'
session = '01'
raw_fname = os.path.join(data_path, 'MEG', 'sample',
                                    'sample_audvis_run{}_ses{}_raw.fif'.format(run, session))
raw_snippet.save(raw_fname, overwrite=True)

# Run 01, Session 02
raw_snippet = raw.copy().crop(120, 180)  
run = '01'
session = '02'
raw_fname = os.path.join(data_path, 'MEG', 'sample',
                                    'sample_audvis_run{}_ses{}_raw.fif'.format(run, session))
raw_snippet.save(raw_fname, overwrite=True)

# Run 02, Session 02
raw_snippet = raw.copy().crop(180, 240)  
run = '02'
session = '02'
raw_fname = os.path.join(data_path, 'MEG', 'sample',
                                    'sample_audvis_run{}_ses{}_raw.fif'.format(run, session))
raw_snippet.save(raw_fname, overwrite=True)

del raw

# move freesurfer results to BIDS-compliant folder, 
# note that if you use the sample data for some other purposes, this might mess up your scripts
freesurfer_path = os.path.join(data_path, 'BIDS','derivatives','freesurfer')
if not os.path.exists(freesurfer_path):    
    os.makedirs(freesurfer_path)
os.system('mv ' + data_path + '/subjects ' + freesurfer_path) #FIXME: copied to the wrong folder!

