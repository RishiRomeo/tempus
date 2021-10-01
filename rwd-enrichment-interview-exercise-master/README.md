###The purpose of this repository is to run a containerized application of a python machine learning model.###


Technical Requirements : 
- Python 3 (recommend Python 3.8)
- Docker version 2.1.0.0 or newer

Technical Recommendations : 
- *nix system


Windows 10 Set up : 
- It is strongly recommended running Ubuntu 18.04 LTS on Windows for ease of set up.
- *If Ubuntu is currently not set up on your machine, follow the steps in Powershell from 
https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package to install 
Windows Subsystem for Linux (WSL)
- In order to have access to 'make' commands, run the following code in your Ubuntu terminal
$ sudo apt-get install build-essential
- Create a new repository and change directory into the new folder
$ mkdir tempus
$ cd tempus
- Unzip the contents of this repository into the new directory or git clone <repo_name>
- Ensure (on local machine) that Docker has WSL integration for Ubuntu-18.04 
(This can be found in your Docker Desktop : Settings > Resources > WSL Integration; Ensure that Ubuntu-18.04 is checked)
- Ensure that you are in the directory containing the Makefile (if unsure, use $ls to look at directory). Run the Makefile
$ make run

