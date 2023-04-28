# MemoryLeakTest


## Scripts

There are two Python scripts in this folder



```bash
memory_limit.py 
```
This script is starting a subprocess and checks it for memory leaks by passing a script and a max. limit of memory to it!

The scripts is checking each 0.1 sec. the size of the virtual memory for the subprocess which is running the passed script.
In this case "memoryLeak.py"

And

```bash
memoryLeak.py 
```
This script contains a simple memory leak. It is adding an integer in an endless loop to a list. The memory gets never cleaned. The OS starts to make a swap after while. So most of the allocated space will land in the virtual memory!

## Usage

The "memory_limit.py" script take two arguments

1. The script that needs to be investigated (which will contain the memory leak)
2. The max. limit of memory that is allowed to allocate for the process

### How to run
1.  Open Terminal and navigate to folder "MemoryLeakTest"
2.  Type in following:
    ```bash
    python memory_limit.py memoryLeak.py [max. memoryLimit in MB]
    ```
    e.g.
    ```bash
    python memory_limit.py memoryLeak.py 4096
    ```
### Outputs

The "memory_limit.py" script will generate two prints. These will be the IDs of the processes. 

e.g

   ```bash
    PROCCESS ID of the submitted code: 77014
    PROCCESS ID of the LeakChecker: 75458
   ```



## Troubleshooting
It is possible, that there occurs an unexpected case, where the memory leak does not get detected. 

In that case you have to stop the process manually by terminating it via CMD

### Terminate process manually

1.  Open Terminal
2. Type in following:
   ```bash
    kill [PROCCESS ID of the submitted code]
   ```
   e.g.
    ```bash
    kill 77014
   ```
This will terminate the script that is causing the memory leak and with that it will also terminate the checker script so "memory_limit.py"


