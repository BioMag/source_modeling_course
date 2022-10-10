"""
==========================================
Run Freesurfer
==========================================

Make sure that Freesurfer is properly configured before running this script.
See the `Setup & Configuration`_ section of the Freesurfer manual.

.. note:: Because of how long the reconstruction takes, this script is set
          up to only regenerate data if necessary. If you want to re-run
          specific steps, then you must delete the resulting files.

.. _Setup & Configuration: https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#Setup.26Configuration  # noqa: E501

Modified from: mne-biomag-group-demo


In the example pipeline freesurfer has already been run. 
Modify this script to suit your own project.

Aalto instructions: 
    
Before starting e.g. spyder, run the following commands in the terminal:
    
module load freesurfer
export FREESURFER_HOME=/work/modules/Ubuntu/14.04/amd64/t314/freesurfer/6.0.0

module load mne
source /work/modules/Ubuntu/14.04/amd64/common/mne/MNE-2.7.4-3434-Linux-x86_64/bin/mne_setup_sh


"""
import os
import os.path as op

import subprocess
import time


from mne.parallel import parallel_func

import mne

from config import (subjects_dir, N_JOBS, subject_info)

from config import study_path 

# Example of subject_info dictionary:
#subject_info = {
#        'sub-s01': 'S01/S8XXX/00002', # subject : rawdata folder (T1-sequence)
#        'sub-s02': 'S02/S8XXX/00002',
#        }

def tee_output(command, log_file):
    print('Running :\n%s' % " ".join(command))
    with open(log_file, 'wb') as fid:
        proc = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            # print(line.decode('utf-8'))
            fid.write(line)
    if proc.wait() != 0:
        raise RuntimeError('Command failed')

def process_subject_anat(subject, subject_id, force_recon_all=False):
    print("Processing %s" % subject)

    t1_fname = op.join(study_path, 'mri', subject_id, 'MR00001')
    print("First file in folder: %s" % t1_fname)
    
    log_fname = op.join(study_path, 'mri', subject_id, 'recon-all-log.txt')
    subject_dir = op.join(subjects_dir, subject)
    
    if op.isdir(subject_dir):
        print('  Skipping reconstruction (folder exists, delete existing if you want to re-run)')
    else:
        print('  Running reconstruction (usually takes hours)')
        t0 = time.time()
        tee_output(
            ['recon-all', '-all', '-s', subject, '-sd', subjects_dir,
             '-i', t1_fname], log_fname)
        print('  Recon for %s complete in %0.1f hours'
              % (subject_id, (time.time() - t0) / 60. / 60.))

def ensure_dir(directory):
  if not os.path.exists(directory):
      os.makedirs(directory)

# Run freesurfer (recon-all)
parallel, run_func, _ = parallel_func(process_subject_anat, n_jobs=N_JOBS)
parallel(run_func(sub,subject_info[sub]) for sub in subject_info)


# Set up mri-images for analysis with mne
for subject in subject_info:
    ensure_dir(subjects_dir +  subject + '/bem/')
    
    ## BEM
    mne.bem.make_watershed_bem(subject, subjects_dir, overwrite=True)
    # Alternatively, use:
    #os.system('mne watershed_bem -s ' + subject + ' -d ' + subjects_dir + ' --overwrite')
    
    ## High-resolution surfaces
    os.system('mne make_scalp_surfaces -s ' + subject + ' -d ' + subjects_dir +' --overwrite --force')
    
    ## Set up COR-file   
    os.system('mne_setup_mri --subject ' + subject + ' --overwrite')
