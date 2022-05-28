from cProfile import label
import psutil
import platform
from datetime import datetime
import socket
import uuid
import re

import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def System_information():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print(f"Ip-Address: {socket.gethostbyname(socket.gethostname())}")
    print(f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")


    # Boot Time
    print("="*40, "Boot Time", "="*40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    print(f"Up Time: {datetime.now() - bt}")


    # print CPU information
    print("="*40, "CPU Info", "="*40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    global cpufreq 
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")


    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")


    # Memory Information
    print("="*40, "Memory Information", "="*40)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")



    print("="*20, "SWAP", "="*20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

    # Disk Information
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")


    def cpuusage():
        cpuusage = np.array(psutil.cpu_percent(interval=1, percpu=True))
        labels = [f"Core {i}" for i in range(len(cpuusage))]
        plt.title("CPU Usage")
        plt.pie(cpuusage, labels=labels, autopct="%1.1f%%")
        plt.show()

    def cpuchart():
        cpuchart = np.array([cpufreq.max, cpufreq.min, cpufreq.current])
        labels = ['Max', 'Min', 'Current']
        plt.title('CPU Frequency')
        plt.pie(cpuchart, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.show() 

    window=tk.Tk()
    window.title("System Information")
    window.geometry("400x700")
    newlabel=tk.Label(window, text="System Information")
    newlabel.grid(column=0, row=0)
    newlabel=tk.Label(window, text="System: "+uname.system)
    newlabel.grid(column=0, row=1)
    newlabel=tk.Label(window, text="Node Name: "+uname.node)
    newlabel.grid(column=0, row=2)
    newlabel=tk.Label(window, text="Release: "+uname.release)
    newlabel.grid(column=0, row=3)
    newlabel=tk.Label(window, text="Version: "+uname.version)
    newlabel.grid(column=0, row=4)
    newlabel=tk.Label(window, text="Machine: "+uname.machine)
    newlabel.grid(column=0, row=5)
    newlabel=tk.Label(window, text="Processor: "+uname.processor)
    newlabel.grid(column=0, row=6)
    newlabel=tk.Label(window, text="Ip-Address: "+socket.gethostbyname(socket.gethostname()))
    newlabel.grid(column=0, row=7)
    newlabel=tk.Label(window, text="Mac-Address: "+':'.join(re.findall('..', '%012x' % uuid.getnode())))
    newlabel.grid(column=0, row=8)
    newlabel=tk.Label(window, text="Boot Time: "+str(bt.year)+"/"+str(bt.month)+"/"+str(bt.day)+" "+str(bt.hour)+":"+str(bt.minute)+":"+str(bt.second))
    newlabel.grid(column=0, row=9)
    newlabel=tk.Label(window, text="Physical Cores: "+str(psutil.cpu_count(logical=False)))
    newlabel.grid(column=0, row=10)
    newlabel=tk.Label(window, text="Total Cores: "+str(psutil.cpu_count(logical=True)))
    newlabel.grid(column=0, row=11)
    newlabel=tk.Label(window, text="Max Frequency: "+str(cpufreq.max))
    newlabel.grid(column=0, row=12)
    newlabel=tk.Label(window, text="Min Frequency: "+str(cpufreq.min))
    newlabel.grid(column=0, row=13)
    newlabel=tk.Label(window, text="Current Frequency: "+str(cpufreq.current))
    newlabel.grid(column=0, row=14)
    newlabel=tk.Label(window, text="Total CPU Usage: "+str(psutil.cpu_percent()))
    newlabel.grid(column=0, row=15)
    newlabel=tk.Label(window, text="Memory Information")
    newlabel.grid(column=0, row=16)
    newlabel=tk.Label(window, text="Total: "+str(get_size(svmem.total)))
    newlabel.grid(column=0, row=17)
    newlabel=tk.Label(window, text="Available: "+str(get_size(svmem.available)))
    newlabel.grid(column=0, row=18)
    newlabel=tk.Label(window, text="Used: "+str(get_size(svmem.used)))
    newlabel.grid(column=0, row=19)
    newlabel=tk.Label(window, text="Percentage: "+str(svmem.percent)+"%")
    newlabel.grid(column=0, row=20)
    newlabel=tk.Label(window, text="Swap Information")
    newlabel.grid(column=0, row=21)
    newlabel=tk.Label(window, text="Total: "+str(get_size(swap.total)))
    newlabel.grid(column=0, row=22)
    newlabel=tk.Label(window, text="Free: "+str(get_size(swap.free)))
    newlabel.grid(column=0, row=23)
    newlabel=tk.Label(window, text="Used: "+str(get_size(swap.used)))
    newlabel.grid(column=0, row=24)
    newlabel=tk.Label(window, text="Percentage: "+str(swap.percent)+"%")
    newlabel.grid(column=0, row=25)
    newlabel=tk.Label(window, text="Disk Information")
    newlabel.grid(column=0, row=26)
    newlabel=tk.Label(window, text="Uptime: "+str(datetime.now() - bt))
    newlabel.grid(column=0, row=27)

    button = tk.Button(window, text="Cpu Usage", command=lambda: cpuusage())
    button.grid(column=0, row=28)
    button = tk.Button(window, text="Cpu Chart", command=lambda: cpuchart())
    button.grid(column=0, row=29)

    window.mainloop()

if __name__ == "__main__":
    System_information()