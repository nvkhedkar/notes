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