import os
import resource
import sys
import subprocess
import time
import signal
import psutil


if len(sys.argv) != 3:
    print("Usage: python memory_limit.py <file_to_check> <memory_limit_in_bytes>")
    sys.exit(1)

file_to_check = sys.argv[1]
memory_limit = int(sys.argv[2])

# Run the file to check
subprocess = subprocess.Popen(['python', file_to_check])
pid_sub = subprocess.pid
pid_checker = os.getppid()
print("PROCCESS ID of the submitted code: "+str(pid_sub))
print("PROCCESS ID of the LeakChecker: "+str(pid_checker))
# Check memory usage every 0.1 seconds
while subprocess.poll() is None:
    usage = psutil.Process(pid_sub).memory_info().vms / (1024 * 1024)

    #fullUsage = (usage.uss / (1024*1024)) + ( usage.swap /(1024* 1024))
   
    #print("Used MEMORY: "+str(usage))
    if usage > memory_limit:
       
        # Kill the subprocess
        os.kill(pid_sub, signal.SIGKILL)
        break
    time.sleep(0.1)