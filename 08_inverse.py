#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Calculate MNE inverse
"""
from __future__ import print_function
import mne
import argparse
import os
from mne.minimum_norm import make_inverse_operator, apply_inverse

from config import (fname, spacing)


# Be verbose
mne.set_log_level('INFO')

# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject', metavar='sub###', help='The subject to process')
parser.add_argument('-ses', help='The session to process')
parser.add_argument('-task', help='The session to process')
args = parser.parse_args()
subject = args.subject
ses = args.ses
task = args.task
 
print('Processing subject:', subject)
print('Processing task:', task)

if task=='audvis':
    from settings_sample import (conditions, baseline)
#elif task=='xxxx':
#    from settings_xxxx import (conditions, baseline)
else:
    print('Undefined task')

# Read the forward model, one model has been created for each session
fwd = mne.read_forward_solution(fname.fwd(subject=subject, ses=ses, task='audvis', run='01', spacing=spacing))
fwd = mne.convert_forward_solution(fwd, surf_ori=True) # do or don't?

# Read the noise covariance matrix
noise_cov = mne.read_cov(fname.noise_cov(subject=subject, ses=ses, task=task))

# Read the info structure
info = mne.io.read_info(fname.epochs(subject=subject, ses=ses, task=task))        

# Compute inverse operator
pick_ori = None # 'normal' or None
snr = 3.0 
lambda2 = 1.0 / snr ** 2
method = "dSPM"

# Create inverse operator in individual subject
if not os.path.exists(fname.inv(subject=subject, ses=ses, task=task)):
    inverse_operator = make_inverse_operator(info = info, 
                                         forward = fwd, 
                                         noise_cov = noise_cov, 
                                         loose = 0.3, 
                                         depth = 0.8) 
    if not os.path.exists(fname.megprocessed_dir(subject=subject, ses=ses) + 'inverse/'):
        os.makedirs(fname.megprocessed_dir(subject=subject, ses=ses) + 'inverse/' )
    mne.minimum_norm.write_inverse_operator(fname.inv(subject=subject,
                                     ses=ses,
                                     task=task), inverse_operator)
else:
    inverse_operator = mne.minimum_norm.read_inverse_operator(
                    fname.inv(subject=subject,
                              ses=ses,
                              task=task))
 


# Compute inverse for all conditions   

# Read the evoked response
evokeds = mne.read_evokeds(fname.evoked(subject=subject,ses=ses,task=task), 
                                          baseline=baseline, proj = True) 
    
if not os.path.exists(fname.megprocessed_dir(subject=subject, ses=ses) + 'stcs/'):
        os.makedirs(fname.megprocessed_dir(subject=subject, ses=ses) + 'stcs/')
   
stcs = dict()
for num,condition in enumerate(conditions):
        print('Computing stcs for condition:', condition)
        stcs[condition] = apply_inverse(evokeds[num],inverse_operator, lambda2, method, pick_ori=pick_ori)
        stcs[condition].save(fname.stc(condition=condition, subject=subject, ses = ses, task=task))
