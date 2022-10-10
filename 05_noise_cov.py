# -*- coding: utf-8 -*-

"""
Create the noise covariance matrix for the inverse solution.

"""

import argparse
import mne
import numpy as np
import os.path as op
import os

from config import (fname, default_baseline, reject, tasks)


# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject',  help='The subject to process')
parser.add_argument('-ses', help='The session to process. ')
#parser.add_argument('-task', help='The task to process. ')
args = parser.parse_args()
subject = args.subject
ses = args.ses
#task = args.task

print('Processing subject: ', subject)
print('Processing session: ', ses)

for task in tasks:
    print('Processing task: ', task)
          
    # Get epochs
    epochs = mne.read_epochs(fname.epochs(subject=subject,ses=ses,task=task,
                                      preload=True, reject=reject, 
                                      proj=False, baseline=default_baseline))

    # Apply same ICA, same filters as for evoked responses
    # load ica
    # apply ica
    # Assumes now that epochs have already been cleaned
                         
    # Calculate noise covariance on baseline time period

    # Check rank estimation!!!!
    noise_cov = mne.compute_covariance(epochs.crop(None, 0), rank='info') 
    noise_cov = mne.cov.regularize(noise_cov, epochs.info, mag=0.05, grad=0.05, proj=False) 

    # Save noise covariance matrix

    # Create folder if it does not exist
    if not os.path.exists(fname.megprocessed_dir(subject=subject, ses=ses) + 'noise_cov/'):  
        os.makedirs(fname.megprocessed_dir(subject=subject,ses=ses) + 'noise_cov/')

    mne.write_cov(fname.noise_cov(subject=subject, ses=ses, task=task), noise_cov)



      
