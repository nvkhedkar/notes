# Ubuntu

1. [Find a word in all files](#find-a-word-in-all-files)
1. [Find release on ubuntu](#find-release-on-ubuntu)
1. [User should not need password](#user-should-not-need-password)
1. [Cpu info](#cpu-info)
1. [Nvidia gpu info](#nvidia-gpu-info)
1. [Find command](#find-command)

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
newuser ALL=(ALL) NOPASSWD:ALL

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
