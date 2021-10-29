# Virtualization

## VirtualBox  

### Windows 10 virtual machine does not get created
**Error message:** Call to WHvSetupPartition failed: ERROR_SUCCESS (Last=0xc000000d/87) (VERR_NEM_VM_CREATE_FAILED).  
[Solution](https://forums.virtualbox.org/viewtopic.php?f=6&t=93443)  
To make these settings:
1. Hit `Win + R` key - to open `run` menu
2. Type `optionalFeatures` - this opens the "Turn Windows features on or off" menu
3. Then turn the features described in the link on/off  
Done

### Start clipboard
```
VBoxClient --clipboard
```

### Update disk uuid
```
C:\Program Files\Oracle\VirtualBox610>VBoxManage internalcommands sethduuid “C:\virtualbox\nk-ubuntu-18.04-base-amd64-150g.vdi”
```

### Using local vagrant box

#### Package virtualbox machine into box - box created in current dir
```
vagrant package --base vagrant1_default_1552542834412_22432 --output ubuntu-18.04-base-amd64.box
```

#### Add the box to vagrant
```
vagrant box add ubuntu-18.04-base-amd64 file:///e:/VirtualBox/myboxes/ubuntu-18.04-base-amd64.box
```

#### To use the box: Init the box:
```
vagrant init ubuntu-18.04-base-amd64 
```
This addes vagrantfile in dir and now vagrant up can be used to start the box

#### Change disk size
VBoxManage.exe clonemedium D:\virtualbox\disk_dir\ubuntu-20.04-desktop-amd64-disk001.vmdk ubuntu-20.04-desktop-amd64-disk001.vdi --format vdi --variant standard
VBoxManage.exe modifymedium D:\virtualbox\disk_dir\ubuntu-20.04-desktop-amd64-disk001.vdi --resize 150100

