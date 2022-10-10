"""
Morph source estimates to same source space (fsaverage) and save morphed stcs to disk.
"""
from __future__ import print_function

import argparse
import numpy as np
import mne
import os

from config import (fname, subjects_dir, subjects, spacing)

# Be verbose
mne.set_log_level('INFO')


tasks = ['audvis']
sessions = ['01', '02']


for subject in subjects:
    for session in sessions:
        print('Processing session:', session)
        for task in tasks:
            print('Processing task:', task)
           
                
            if task=='audvis':
                from settings_sample import (conditions, baseline)
            #elif task=='xxxx':
            #    from settings_xxxx import (conditions, baseline)
            else:
                print('Undefined task')                
            
            for condition in conditions:
                print('Processing condition:', condition)
                
                print('Processing subject:', subject)
                #Read stc
                stc_fname = fname.stc(subject=subject,task=task,condition=condition, ses=session)
                stc_subject = mne.read_source_estimate(stc_fname)
                
                #Read source space
                fwd = mne.read_forward_solution(fname.fwd(subject=subject,task=task,run='01', spacing=spacing, ses=session))
                src_from=fwd['src']
                
                #Calculate morph
                morph = mne.compute_source_morph(src_from, subject_from=subject,
                                         subject_to='fsaverage',
                                         subjects_dir=subjects_dir, spacing=5, smooth=10)
         
                # Morph the STC to the fsaverage brain.
                #from ico-4 to ico-5!        
                #stc_subject.subject = 'sub-'+subject
                stc_fsaverage = morph.apply(stc_subject)
        
                stc_fsaverage.save(fname.stc_morphed(subject=subject,
                                                     task=task,
                                                     condition=condition, 
                                                     ses=session), overwrite=True)