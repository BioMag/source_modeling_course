Tested on Windows 10 and Ubuntu 22.04 LTS.

# Install miniconda

# Create MNE environment
The environment contains mne + some useful packages (numpy, matplotlib, etc). Change to the folder that contains the environment.yml file and run  
`conda env create`

# Install Spyder
Install the spyder package + some optional dependencies recommended by the author.  
`conda create -n spyder spyder numpy scipy pandas matplotlib sympy cython`  
  
On Ubuntu, add PyQtWebEngine to the list of packages to be installed  
`conda create -n spyder spyder numpy scipy pandas matplotlib sympy cython PyQtWebEngine`

# Setup Spyder
Open spyder. From the miniconda prompt run  
`conda activate spyder`  
`spyder`  
  
Setup Spyder to use python interpreter from the mne environment. In Spyder: Tools -> Preferences -> Python interpreter -> Use the following Python intepreter -> select the interpreter for the mne environment.  
  
Setup Spyder to plot graphs in separate windows: In Spyder: Tools -> Preferences -> IPython console -> Graphics -> Backend -> Qt5.  
Restart Spyder.  

# Install FreeSurfer
Doesn't work on Windows. Install tcsh  
`sudo apt install tcsh`  

Download freesurfer-linux-ubuntu22_amd64-7.3.2.tar.gz to ~/opt  
`cd ~/opt`  
`tar -zxpf freesurfer-linux-ubuntu22_amd64-7.3.2.tar.gz`  

Copy the .license file to ~/opt/freesurfer  

Move the subjects dir to ~/freesurfer_subjects  
`mv ~/opt/freesurfer/subjects ~/freesurfer_subjects`

Add the following lines to ~/.bashrc  
`export FREESURFER_HOME=$HOME/opt/freesurfer`  
`export SUBJECTS_DIR=$HOME/freesurfer_subjects`  
`source $FREESURFER_HOME/SetUpFreeSurfer.sh`
