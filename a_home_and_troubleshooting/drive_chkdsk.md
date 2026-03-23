
Here is a comprehensive troubleshooting guide based on our session. You can copy this into a `.md` file (e.g., `USB_Repair_Guide.md`) and keep it in your Raspberry Pi's home directory for future reference.

***

## USB Drive Troubleshooting Guide (Windows to Raspberry Pi)

This guide addresses "Ghosting" issues where a USB drive works on Windows but is not detected or fails to mount on a Raspberry Pi, specifically after power fluctuations or improper shutdowns.

### Phase 1: Windows Hardware & Logic Check
Before moving to the Pi, ensure the drive's internal "health" and "paperwork" (File System) are intact.

1.  **Hardware Verification:**
    * Open **SeaTools 5**.
    * Run a **Short Generic Test**.
    * *Result:* If it **Passes**, the physical motor and platters are healthy. If it **Fails**, the drive is physically dying; back up data immediately.

2.  **Identify the Errors (Read-Only):**
    * Open Command Prompt as **Administrator**.
    * Run: `chkdsk X: /v` (Replace `X` with your drive letter).
    * *Look for:* "File record segment XXXX is corrupt" or "Errors found."

3.  **Execute the Repair:**
    * Run the "Deep Fix" command:
        ```cmd
        chkdsk X: /f /x
        ```
    * **`/f`**: Fixes errors on the disk.
    * **`/x`**: Forces a dismount so the Master File Table (MFT) can be rebuilt.
    * *Result:* Look for "Windows has made corrections to the file system."

4.  **The "Clean Break":**
    * **CRITICAL:** Always right-click the drive in Taskbar and select **"Safely Remove Hardware / Eject."** Failure to do this sets the "Dirty Bit," which causes the Pi to reject the drive again.

---

### Phase 2: Raspberry Pi Integration
Once the drive is "Clean" from Windows, move it to the Pi.

1.  **Hardware Detection:**
    * Plug the drive in and run:
        ```bash
        lsblk
        ```
    * Confirm your drive appears (usually as `sda` or `sdb` with a partition like `sda1`).

2.  **Kernel Log Check (The "Why"):**
    * If the drive isn't appearing, check the system logs for power or connection errors:
        ```bash
        sudo dmesg | tail -n 20
        ```
    * *Look for:* "Under-voltage detected" or "USB disconnect."

3.  **Clearing the "Dirty Bit" (Force Mount):**
    * If the Pi sees the drive but won't mount it, run:
        ```bash
        sudo ntfsfix -d /dev/sda1
        ```
    * *Note:* Replace `sda1` with your actual identifier from `lsblk`.

4.  **Manual Mount:**
    ```bash
    sudo mkdir -p /mnt/usb
    sudo mount /dev/sda1 /mnt/usb
    df -h
    ```

---

### Phase 3: Power Surge Prevention
To prevent "File Record Segment" corruption in the future:

* **Inverter Settings:** Switch your home inverter from **"Eco/Home Mode"** to **"UPS Mode"**. This reduces the switchover delay from ~20ms to ~10ms, which is often fast enough to save the Pi's filesystem.
* **Write Syncing:** Add the `sync` flag to your `/etc/fstab` entry for this drive to ensure data is written immediately to the disk rather than held in volatile RAM cache.
* **Hardware:** Use the **Official Raspberry Pi Power Supply**, as it has better capacitors to bridge minor voltage ripples.

---
**Status:** File System Repaired | Hardware Healthy | Ready for Pi.