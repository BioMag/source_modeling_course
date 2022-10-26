#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with FreeSurfer - tet's take care of the anatomy
"""


#%% Cell #0
""" Now we need to do a couple of things outside of Spyder.

    1. Make sure that FreeSurfer is installed and find the subjects directory.
    2. Make sure the subjects directory doesn't have a subject called 'sample'.
    3. Check that we have a valid MR file (e.g. with freview)
    4. Create a subject called 'sample' with MRI file 'MRI.mgz'
       > recon-all -i ~/source_modeling_course/data/MEG/MRI.mgz -subjid sample
    5. Check that the subject 'sample' is created.
    6. Run the full FreeSurfer pipeline
       > recon-all -all -subjid sample
       The pipeline runs for several hours, so we will cheat by copying 
       ~/source_modeling_course/data/precomputed/sample to the
       subjects folder.
"""


#%% Cell #1
""" MNE integrates with FreeSurfer through the subjects folder. As long as
    the system variable $SUBJECTS_DIR points to the correct location, you can
    refer to FreeSurfer subjects from inside MNE by their subject ids.
    
    Let's check the we can access the 'sample' subject
"""
import mne
Brain = mne.viz.get_brain_class()   # Note that Brain is a class, not an 'usual' instance

# 'sample' is a FreeSurfer subject id
brain = Brain('sample', surf='inflated', size=(800, 600))    # What happens if we use surf='pial'? 'smoothwm'?
brain.add_annotation('aparc.a2009s', borders=False)


#%% Cell #4
""" Now we need to create BEMs ...
"""
import mne
mne.bem.make_watershed_bem('sample')
""" Note that we are running a FreeSurfer command here
"""


#%% 
""" ... and look at them
"""
mne.viz.plot_bem('sample')