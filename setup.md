# Install miniconda

# create MNE environment
conda create --override-channels --channel=conda-forge -n mne mne python=3.10 spyder‑kernels=2.2

# Install Spyder
conda create -n spyder spyder numpy scipy pandas matplotlib sympy cython PyQtWebEngine
