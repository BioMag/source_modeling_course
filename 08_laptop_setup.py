#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In case you want to continue analysis on your own laptop
"""


#%% Cell #0
""" Create a folder for FreeSurfer subjects (e.g. 'freesurfer_subjects') and
    copy the 'sample' subject there.
"""
 

#%% Cell #1
"""
    Make sure that it is accessible through 'SUBJECTS_DIR' config
"""
import mne
mne.get_config('SUBJECTS_DIR')


#%% Cell #2
""" In case it is not defined ('get_config' produced no output), set it through
    MNE config. Note that the variables set with 'mne.set_config' are
    persistent.
"""
# mne.set_config('SUBJECTS_DIR', '~/freesurfer_subjects') # Linux
# mne.set_config('SUBJECTS_DIR', 'C:/Users/andrey/freesurfer_subjects') # Windows


#%% Cell #3
""" If everything has been set up correctly, we should be able to see the brain
    segmentation ...
"""
Brain = mne.viz.get_brain_class()   # Note that Brain is a class, not an 'usual' instance
brain = Brain('sample', surf='inflated', size=(800, 600))    # What happens if we use surf='pial'? 'smoothwm'?
brain.add_annotation('aparc.a2009s', borders=False)


#%% Cell #4
""" ... and BEMs
"""
mne.viz.plot_bem('sample')


#%% Cell #5
""" Create a data folder (e.g. 'C:/Users/andrey/source_modeling_course/data')
    and copy there the folder 'MEG' from  ~/source_modeling_course/data/ folder
    on the BioMag computer.
"""


#%% Cell #6
""" Point it with the 'DATA_DIR'
"""
import os
# mne.set_config('DATA_DIR', os.getenv('HOME') + '/source_modeling_course/data') # on BioMag workstations
# mne.set_config('DATA_DIR', 'C:/Users/andrey/source_modeling_course/data') # on Windows


#%% Cell #7
""" Create a scratch folder (e.g. 'C:/Users/andrey/source_modeling_course/scratch')
    and point it with the 'SCRATCH_DIR'
"""

# mne.set_config('SCRATCH_DIR', os.getenv('HOME') + '/scratch') # on BioMag workstations
# mne.set_config('SCRATCH_DIR', 'C:/Users/andrey/source_modeling_course/scratch') # on Windows


#%% Cell #8
""" Copy the code examples from ~/source_modeling_course/code on the BioMag
    computers to your laptop
"""


#%% Cell #9
""" Finally, we should be able to load and inspect an MEG data file.
"""
INP_FNAME = mne.get_config('DATA_DIR') + '/MEG/sample_audvis_raw.fif'
raw = mne.io.Raw(INP_FNAME, preload=True)
raw.plot()







