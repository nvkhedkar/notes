# Nodejs notes

## Install latest nodejs on ubuntu
```
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
```
To upgrade to latest version (and not current stable) version, you can use
```
sudo n latest
```
Fix PATH
```
sudo apt-get install --reinstall nodejs-legacy     # fix /usr/bin/node
```
To undo:
```
sudo n rm 6.0.0     # replace number with version of Node that was installed
sudo npm uninstall -g n
```
## Links
(rascal rabbitmq intro)[https://www.cloudamqp.com/blog/how-to-run-rabbitmq-with-nodejs.html]
(book - Enterprise integration patterns)[https://www.enterpriseintegrationpatterns.com/]

## Azurite on windows
### Detailed Tutorial: Using Azurite on Windows

Azurite is the modern, open-source emulator for Azure Blob, Queue, and Table storage, designed for local development and testing. It supersedes the classic Azure Storage Emulator and is cross-platform, working on Windows, Linux, and macOS[1][5].

---

### **1. Prerequisites**

- **Node.js** (LTS version recommended)
- **npm** (comes with Node.js)
- **Windows OS**

---

### **2. Install Azurite**


```bash
npm install -g azurite
```
This will make the `azurite` command available in your terminal or command prompt[5][6].

---

### **3. Starting Azurite**

You can start Azurite from the command line with default settings:

```bash
azurite
```

**Customizing Storage Location and Logging**

To specify where Azurite stores data and where it writes logs:

```bash
azurite -l C:\azurite --debug C:\azurite\debug.log
```
- `-l` or `--location`: Directory for Azurite data (e.g., blobs, queues, tables).
- `--debug`: Path for debug logs[5][6].

**Example: Start Azurite Silently with Custom Paths**
```bash
azurite --silent --location C:\azurite --debug C:\azurite\debug.log
```

---

### **4. Running Azurite as a Background Service**

You can create a batch script to start Azurite minimized in the background:

**Create a batch file (`azurite-startup.cmd`):**
```batch
start /B /MIN azurite -l "C:\dev\data\Azurite" --blobHost 0.0.0.0 --blobPort 10000 --queueHost 0.0.0.0 --queuePort 10001 --tableHost 0.0.0.0 --tablePort 10002 > "C:\dev\data\Azurite\azurite.log" 2>&1
```
- This starts all services and writes output to a log file[6].

**Auto-start on Windows Startup:**
- Place the batch file in the Windows Startup folder to run Azurite automatically when you log in[6].

---


### **5. Connecting to Azurite**

- **Default connection string:**
  ```
  UseDevelopmentStorage=true
  ```
  or
  ```
  DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFeqCnf2e...
  BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;
  QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;
  TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;
  ```
- Use these endpoints in your application configuration to connect to Azurite locally.

---

### **6. Advanced: Running Individual Services**

You can run only specific services (blob, queue, or table):

```bash
azurite-blob -l C:\azurite
azurite-queue -l C:\azurite
azurite-table -l C:\azurite
```
This is useful if you only need one type of storage[5].

---

### **8. Stopping Azurite**

- If started in a terminal, press `Ctrl+C` to stop.
- If running as a background process, end it via Task Manager or close the command window.

---

### **Summary Table: Common Azurite Commands**

| Command                                                    | Description                                 |
|------------------------------------------------------------|---------------------------------------------|
| `npm install -g azurite`                                   | Install Azurite globally                    |
| `azurite`                                                  | Start Azurite with default settings         |
| `azurite -l C:\azurite --debug C:\azurite\debug.log`       | Custom data/log location                    |
| `azurite-blob -l C:\azurite`                               | Start only Blob service                     |
| `azurite-queue -l C:\azurite`                              | Start only Queue service                    |
| `azurite-table -l C:\azurite`                              | Start only Table service                    |

---

## **References**

- [Microsoft Docs: Use Azurite emulator for local Azure Storage development][1]
- [Azurite GitHub Repository][5]
- [Running Azurite on Windows Startup][6]

---

Azurite is a robust and flexible emulator for Azure Storage, making local development and testing seamless and efficient on Windows.

[1] https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite
[2] https://www.youtube.com/watch?v=V6iOFfi8VwY
[3] https://stackoverflow.com/questions/76870582/how-can-i-use-azurite-in-a-command-line-application
[4] https://learn.microsoft.com/en-us/azure/storage/common/storage-use-emulator
[5] https://github.com/Azure/Azurite
[6] https://dev.to/kkoziarski/running-azurite-emulator-in-background-on-windows-startup-1nke
[7] https://www.youtube.com/watch?v=FO6MsKal96Y
[8] https://www.ccslearningacademy.com/azure-storage-emulator/
