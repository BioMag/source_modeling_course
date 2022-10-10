"""
Compute average of the power maps of morphed source estimates.
"""
from __future__ import print_function


import numpy as np
import mne
import os

from config import (fname, subjects_dir, subjects,  spacing, tasks, sessions)


# Be verbose
mne.set_log_level('INFO')


# Be verbose
mne.set_log_level('INFO')


for task in tasks:
    print('Processing task:', task)
    
    if task=='audvis':
        from settings_sample import (conditions, baseline)
    #elif task=='xxxx':
    #    from settings_xxxx import (conditions, baseline)
    else:
        print('Undefined task')
    
        
    for session in sessions:
        print('Processing session:', session)
        for condition in conditions:
            print('Processing condition:', condition)
            stcs = list()
        
            for subject in subjects:
                print('Reading subject:', subject)
                stc_morphed_fname = fname.stc_morphed(subject=subject,task=task,condition=condition, ses=session)
                stc_fsaverage = mne.read_source_estimate(stc_morphed_fname)
                stcs.append(stc_fsaverage)
                    
            # Average the source estimates
            print('Saving grand average')
            
            data = np.mean([stc.data for stc in stcs], axis=0)
            ga_stc = mne.SourceEstimate(data, vertices=stcs[0].vertices,
                                        tmin=stcs[0].tmin, tstep=stcs[0].tstep)
            
            # Calculate and save evoked responses
            if not os.path.exists(fname.megprocessed_dir(subject='GA'+group, ses=session) + 'stcs/'):    
                os.makedirs(fname.megprocessed_dir(subject='GA'+group,ses=session) + 'stcs/')
         
            ga_stc.save(fname.stc(subject='GA'+group,task=task, condition=condition, ses=session), overwrite=True)

