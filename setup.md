# Install miniconda

# Create MNE environment
The environment contains mne + some useful packages (numpy, matplotlib, etc). Change to the folder that contains the environment.yml file and run  
`conda env create`

# Install Spyder
Install the spyder package + some optional dependencies recommended by the author.  
`conda create -n spyder spyder numpy scipy pandas matplotlib sympy cython PyQtWebEngine`

# Setup Spyder to use python interpreter from the mne environment

# Install FreeSurfer
Download freesurfer-linux-ubuntu22_amd64-7.3.2.tar.gz to ~/opt  
`cd ~/opt`  
`tar -zxpf freesurfer-linux-ubuntu22_amd64-7.3.2.tar.gz`  

Add the following two lines to ~/.bashrc  
`export FREESURFER_HOME=$HOME/opt/freesurfer`  
`source $FREESURFER_HOME/SetUpFreeSurfer.sh`
