import os
import psutil
import signal


def kill_if_max_memory_exceeded(pid,max_mem_gb):
    limit = int(max_mem_gb * 1024**3)  
    proc = psutil.Process(pid)
    rss = proc.memory_info().rss
    if rss > limit:
        print(f"Memory exceeded: {rss / (1024**3):.2f} GiB")
        os.kill(os.getpid(), signal.SIGKILL)

