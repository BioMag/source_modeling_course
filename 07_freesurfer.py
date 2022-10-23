#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with FreeSurfer
"""

#%%
""" We start with two files -- MEG and anatomical MRI. The MEG file should
    contain the data needed for the coregistration (at least, the locations of
    fiducial points).
"""


#%% Cell #0
""" Load and inspect an MEG data file - it's quite similar to EEG
"""
import mne
INP_FNAME = '~/source_modeling_course/data/MEG/sample_audvis_raw.fif'
raw = mne.io.Raw(INP_FNAME, preload=True)
raw.plot()


#%% Cell #1
""" Look at the MRI
"""
import os
import nibabel as nib
# Remember to replace 
MRI_FNAME = '%s/source_modeling_course/data/MEG/MRI.mgz' % os.getenv('HOME')
mri = nib.load(MRI_FNAME)
mri.orthoview()


#%% Cell #2
""" Now we need to do a couple of things outside of Spyder.

    1. Make sure that FreeSurfer is installed and find the subjects directory.
    2. Make sure the subjects directory doesn't have a subject called 'sample'.
    3. Create a subject called 'sample' with MRI file 'MRI.mgz'
       > recon-all -i ~/source_modeling_course/data/MEG/MRI.mgz -subjid sample
    4. Check that the subject 'sample' is created.
    5. Run the full FreeSurfer pipeline
       > recon-all -all -subjid sample
       The pipeline runs for several hours, so we will cheat by copying 
       ~/source_modeling_course/data/precomputed/sample to the
       subjects folder.
"""


#%% Cell #3
""" MNE integrates with FreeSurfer through the subjects folder. As long as
    the system variable $SUBJECTS_DIR points to the correct location, you can
    refer to FreeSurfer subjects from inside MNE by their subject ids.
    
    Let's check the we can access the 'sample' subject
"""
Brain = mne.viz.get_brain_class()   # Note that Brain is a class, not an 'usual' instance

# 'sample' is a FreeSurfer subject id
brain = Brain('sample', surf='inflated', size=(800, 600))    # What happens if we use surf='pial'? 'smoothwm'?
brain.add_annotation('aparc.a2009s', borders=False)


#%% Cell #4
""" Now we need to create BEMs ...
"""
mne.bem.make_flash_bem('sample')
# You cal also try mne.bem.make_watershed_bem('sample'), but this one takes
# longer

""" ... and look at them
"""
mne.viz.plot_bem('sample')


#%% Cell #5
""" Next, we need to coregister MRI and MEG. Run
    > mne coreg
    from the mne conda environment and save the results to
    ~/scratch/sample_audvis_raw-trans.fif
"""
