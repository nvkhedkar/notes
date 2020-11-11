# Python code snippets

## Kill process started with shell=True
```
import os
import signal
import subprocess

# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.
pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                       shell=True, preexec_fn=os.setsid) 

os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
```

## Gracefully handle signal termination
```
import signal
import time

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

if __name__ == '__main__':
  killer = GracefulKiller()
  while not killer.kill_now:
    time.sleep(1)
    print("doing something in a loop ...")

  print("End of the program. I was killed gracefully :)")
``` 