# Install miniconda

# create MNE environment
conda create --override-channels --channel=conda-forge -n mne mne

# Install spyder-kernels
conda activate mne
conda install spyder‑kernels=2.3

# Install Spyder
conda create -n spyder spyder numpy scipy pandas matplotlib sympy cython PyQtWebEngine

# Setup Spyder to use python interpreter from the mne environment

# Install FreeSurfer
Copy freesurfer-linux-ubuntu20_amd64-7.3.2.tar.gz to ~/opt
cd ~/opt
tar -zxpf freesurfer-linux-ubuntu20_amd64-7.3.2.tar.gz
Add the following two lines to ~/.bashrc
export FREESURFER_HOME=$HOME/opt/freesurfer
source $FREESURFER_HOME/SetUpFreeSurfer.sh