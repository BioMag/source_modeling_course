"""
Create source space and compute forward solution

Author: mli
"""
from __future__ import print_function
import os
import argparse

import mne

from config import (fname, subjects_dir, spacing, N_JOBS,  proc, sessions)

# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject', help='The subject to process')
args = parser.parse_args()
subject = args.subject


print('Processing subject: ', subject)


if spacing=='ico4':
    ntri=5120
    ico=4
elif spacing=='ico5':
    print('ico5')
    ntri=20484 #check or 20480
    ico=5

# Saves bem model 
for ses in sessions:
    print('Processing session: ', ses)
    megdir=fname.megprocessed_dir(subject=subject, ses=ses)

    # Create folder if it does not exist
    if not os.path.exists(fname.megprocessed_dir(subject=subject, ses=ses) + 'forward/'):  
        os.makedirs(fname.megprocessed_dir(subject=subject,ses=ses) + 'forward/')
        
    # Create source space in individual subject 
    if not os.path.exists(fname.src(megprocessed_dir=megdir, subject=subject, spacing=spacing)):
        subject_src = mne.setup_source_space(subject=subject, spacing=spacing,
                                       subjects_dir=subjects_dir,
                                       n_jobs=N_JOBS, add_dist=True)
        mne.write_source_spaces(fname.src(megprocessed_dir=megdir, subject=subject,spacing=spacing), subject_src, overwrite=True)
    else:
        subject_src = mne.read_source_spaces(fname.src(megprocessed_dir=megdir, subject=subject,sp=spacing))

    # Create BEM model
    if not os.path.exists(fname.bem_sol(megprocessed_dir=megdir, subject=subject,ntri=ntri)):
        bem_model = mne.make_bem_model(subject=subject, ico=ico, subjects_dir=subjects_dir,
                               conductivity=(0.3,))
        if bem_model[0]['ntri'] == ntri:            
            bem = mne.make_bem_solution(bem_model)
            mne.write_bem_solution(fname.bem_sol(megprocessed_dir=megdir, subject=subject,ntri=bem_model[0]['ntri']),bem)
        else:
            raise ValueError('ntri should be %d' % (ntri))
    else:
        bem=mne.read_bem_solution(fname.bem_sol(megprocessed_dir=megdir, subject=subject,ntri=ntri))


    #Create the forward model, coregistration required (trans_file)
    # Use first run in one of the tasks for forward model
    run = '01'
    task='audvis'

    megdir=fname.megprocessed_dir(subject=subject, ses=ses)
        
    info = mne.io.read_info(fname.raw(subject=subject, ses=ses, task=task, proc=proc, run=run))
    fwd = mne.make_forward_solution(
        info,
        trans=fname.trans_file(subject= subject, ses=ses, megprocessed_dir=megdir),
        src=subject_src,
        bem=bem,
        meg=True,
        eeg=False,
        mindist=0,
        n_jobs=N_JOBS
        )

    mne.write_forward_solution(fname.fwd(subject=subject,ses=ses,task=task, run=run, spacing=spacing), fwd,
                                   overwrite=True)    

