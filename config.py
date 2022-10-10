"""
===========
Config file
===========

Configuration parameters for the study.
"""

import os
from fnames import FileNames

# Test on sample data
# Re-run download_example_data.py if the files have been corrupted


# Your own path
#data_path = '/projects/myproject/'

user = os.environ['USER']

study_path = "/projects/BioMag_pipelines/MNE-sample-data/"

N_JOBS = 4

# Preprocessing with maxfilter
proc = 'tsss' 

# Rejection limits
reject = dict(mag=4e-12, grad=3000e-13)#, eog=150e-6) 

# Default baseline window
default_baseline = (-0.2,0)

# Source spacing 
spacing = 'ico4'

sessions=['01','02']

tasks = ['audvis']

session1 = {'audvis'   :['01','02'], 
#         'restEO'   :['01'], # other tasks included in you experiment
#         'restEC'   :['01'],
#         'emptyroom':['01']
         }

session2 = {'audvis'   :['01','02'], 
#         'restEO'   :['01','02'], # other tasks included in you experiment
#         'emptyroom':['01']
         }
###############################################################################
# Folders (TODO: decide on folder structure)

data_path = os.path.join(study_path, 'BIDS/')
processed_dir = os.path.join(study_path,'processed/')

#BIDS compatible subjects_dir:
subjects_dir = os.path.join(data_path, 'derivatives/', 'freesurfer/')

#The sample data stores the freesurfer results in:
#subjects_dir = os.path.join(data_path, 'subjects/')

os.environ["SUBJECTS_DIR"] = subjects_dir


###############################################################################
# Subjects

subjects=['01'] # sample subject changed to '01' in bidsification

# Subject-codes for freesurfing
subject_info = {
        'sub-s01': 'S01/SNNNN/00002', # folder-structure for raw mris, here the T1 sequence is in folder 00002
        }

###############################################################################
# Templates for filenames
fname = FileNames()

# Some directories
fname.add('data_path', data_path)
fname.add('megbids_dir','{data_path}/{subject}/ses-{ses}/meg/')
fname.add('subjects_dir', subjects_dir)
fname.add('processed_dir', processed_dir)
fname.add('megprocessed_dir','{processed_dir}{subject}/ses-{ses}/meg/')

# Add these so we can use them in the filenames
fname.add('spacing', spacing)

# Maxfilter
fname.add('pos', '{megbids_dir}/{subject}_ses-{ses}_task-{task}_run-{run}_movecomp.pos')
fname.add('tsss_log', '{megbids_dir}/{subject}_ses-{ses}_task-{task}_run-{run}_tsss_log.log')

# Sensor-level files
fname.add('raw', '{megbids_dir}/{subject}_ses-{ses}_task-{task}_run-{run}_proc-{proc}_meg.fif')
fname.add('epochs', '{megprocessed_dir}/epochs/{subject}_ses-{ses}_task-{task}-epo.fif')
fname.add('epochs_proc', '{megprocessed_dir}/epochs/{subject}_ses-{ses}_task-{task}_proc-{proc}-epo.fif')
fname.add('evoked', '{megprocessed_dir}/evoked/{subject}_ses-{ses}_task-{task}-ave.fif')

# Artefact removal
fname.add('ica', '{megprocessed_dir}/ica/{subject}_ses-{ses}_task-{task}_{method}-ica.fif')
          
# Coregistration files (WIP)          
fname.add('fid', '{subjects_dir}/{subject}/bem/{subject}-fiducials.fif')
fname.add('trans_file', '{megbids_dir}/{subject}_ses-{ses}_coreg-transfile.fif')
fname.add('trans_file_old', '{subjects_dir}/{subject}/mri/T1-neuromag/sets/COR-transfile.fif')
fname.add('coreg_log', '{megprocessed_dir}/forward/coreg_log_{subject}_ses-{ses}_hs.csv')

# Source space and forward model          
fname.add('bem_sol', '{megprocessed_dir}/forward/{subject}-{ntri}-bem-sol.fif')
fname.add('fwd', '{megprocessed_dir}/forward/{subject}_ses-{ses}_task-{task}_run-{run}-{spacing}-fwd.fif')
fname.add('src', '{megprocessed_dir}/forward/{subject}-{spacing}-src.fif')

# Inverse solution
fname.add('noise_cov', '{megprocessed_dir}/noise_cov/{subject}_ses-{ses}_task-{task}_cov.fif')
fname.add('inv', '{megprocessed_dir}/inverse/{subject}_ses-{ses}_task-{task}-{spacing}-inv.fif')

# STC-files
fname.add('stc_hemi', '{megprocessed_dir}/stcs/{subject}_ses-{ses}_task-{task}-{condition}-{hemi}.stc')
fname.add('stc', '{megprocessed_dir}/stcs/{subject}_ses-{ses}_task-{task}-{condition}')

