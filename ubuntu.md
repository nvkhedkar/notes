# Ubuntu

1. [Find a word in all files](#find-a-word-in-all-files)
1. [Find release on ubuntu](#find-release-on-ubuntu)
1. [User should not need password](#user-should-not-need-password)
1. [Cpu info](#cpu-info)
1. [Nvidia gpu info](#nvidia-gpu-info)
1. [Find command](#find-command)
1. [Install docker](#installdocker)

## Find a word in all files
```
grep -r -l startElastic .
```
>-r : recursive search  
>-l : include only filenames 

```
grep -r -l -i my_name --include \*.py .
```
-r : recursive  
-l : include only filenames  
-i : case insensative  
my_name : the pattern  
--include \\*.py : Search only in .py files   

## du without "Permission denied"
```
du -h . --max-depth=1 2> >(grep -v 'Permission denied') | sort -n
```
## list only top 5 files
```
ls -lth | head -5
```
## Find release on ubuntu
Command  
```
cat /etc/os-release
```
Output  
```
NAME="Ubuntu"
VERSION="18.04.3 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.3 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

## User should not need password
To setup a user `newuser` so that the user is not asked for password when running commands.
```
sudo usermod -aG sudo newuser
```
This adds the user to `sudo` group.  
Now add the following line at the endof `/etc/sudoers` file
```
#includedir /etc/sudoers.d
newuser ALL=(ALL:ALL) NOPASSWD:ALL

```
After this `newuser` will not be asked for passwords.

## Cpu info
```
lscpu | egrep 'Model name|Socket|Thread|NUMA|CPU\(s\)'
```
Gives:
```
CPU(s):              6
On-line CPU(s) list: 0-5
Thread(s) per core:  1
Socket(s):           1
NUMA node(s):        1
Model name:          Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz
NUMA node0 CPU(s):   0-5
```
## Nvidia gpu info

#### Gpu name
```
nvidia-smi --query-gpu=name --format=csv,noheader
```
This will give for `Tesla K80`
```
Tesla K80
```
#### Gpu ram
```
nvidia-smi --query-gpu=memory.total --format=csv,noheader
```
Gives:
```
11441 MiB
```
#### Gpu driver version
```
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```
Gives:
```
418.87.00
```

#### Gpu usage
```
nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader
nvidia-smi -i 0 --query-gpu=memory.used --format=csv,noheader | awk  '{ print $1 }'
nvidia-smi --query-gpu=count --format=csv,noheader | awk  '{ print $1 }'
nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader
nvidia-smi --query-compute-apps=pid,process_name,gpu_uuid,gpu_name,used_memory --format=csv,noheader,nounits
nvidia-smi --query-compute-apps=pid,process_name,gpu_uuid --format=csv,noheader,nounits
nvidia-smi --query-gpu=index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature.gpu --format=csv,noheader,nounits"
nvidia-smi
```
#### Cuda version
```
cat /usr/local/cuda/version.txt
```
Gives cuda version
```
CUDA Version 10.1.243
```

## Find command
```
find . \( -name '*.pdf' -or -name '*.conf' \)
```
Recursively finds `pdf` and `conf` files
```
find . \( -name '*.pdf' -or -name '*.conf' \) -print
```
Prints the file names
```
find . \( -name '*.pdf' -or -name '*.conf' \) -delete
```
Deletes the files

## Snippets
### Remove ^M
```
perl -p -e 's/\r//g' infile > outfile
```

## Users
### Add user
```
sudo useradd -s /bin/bash -d /home/nkhedkar/ -m -G sudo nkhedkar
```

## PostgreSql
### Check
[stackoverflow link](https://stackoverflow.com/questions/42653690/psql-could-not-connect-to-server-no-such-file-or-directory-5432-error)  
pg_lsclusters: to check status of all clusters  
pg_ctlcluster version cluster start  
pg_ctlcluster 10 main start

## Install/Uninstall
### Uninstall nvidia cuda toolkit
[stackoverflow](https://askubuntu.com/questions/1271418/how-to-purge-or-completely-remove-cuda-from-ubuntu-18-04-and-reinstall-ver-10-2)

Check nvidia driver version when nvidia-smi is not working
```
modinfo nvidia | grep version
```
For checking
```
sudo apt-cache search nvidia | grep cuda
sudo apt-cache search cublas
apt-cache rdepends packagename -> reverse dependencies
apt-cache depends packagename
```

```
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt remove --autoremove nvidia-cuda-toolkit
```

### dpkg stuff
[dpkg cheatsheet](https://www.cyberciti.biz/howto/question/linux/dpkg-cheat-sheet.php)


## Install docker
Install pre-reqs
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```
Add repo
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
```
Update and install
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Check status
```
sudo systemctl status docker
```
Add me to docker group so I can use it
```
sudo usermod -aG docker nkhedkar
```
## Path
Add directory to path  
```
export PATH="/path/to/dir:$PATH"
```
## Multiple ethernets
Before starting the vm - in virtualbox network settings - enable "bridged" and "nat network" both.
Ubuntu 20.04 uses netplan to configure ethernets. At a time only one  `eth#` will be active.  
To activate 2:
```
sudo vi /etc/netplan/01-network-manager-all.yaml
```
Add the following lines
```
  ethernets:
    en01:
      dhcp4: true
      dhcp6: true
```
The final file will look like:
```
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    eth0:
      dhcp4: true
      dhcp6: true
    eth1:
      dhcp4: true
      dhcp6: true
```
The do:
```
sudo netplan apply
```

## nohup
run process in background so closing terminal does not close the process  

```
nohup python myapp.py -a <arg1> -b <arg2> &
```
This appends command output to `nohup.out`.  
To rotate `nohup.out` with logrotate.  
Create /etc/logrotate.d/nohup and add the following:
```
/<path_to_file>/nohup.out {
    size 124k
    copytruncate
    notifempty
    rotate 5
}
```
Direct output to another file
```
nohup command > output.log 2>&1 &
```
Direct output to dev/null
```
nohup command >/dev/null 2>&1 & 
```
