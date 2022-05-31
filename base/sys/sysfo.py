from cProfile import label
from traceback import print_tb
import psutil
import platform
from datetime import datetime
import socket
import uuid
import re

import matplotlib.pyplot as plt
import numpy as np

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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
    plt.autoscale(enable=True, axis='both', tight=True)

global cpufreq 
cpufreq = psutil.cpu_freq() 

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("System Information")
    window.setGeometry(100, 100, 750, 400)
    window.setStyleSheet("background-color: black;")
    window.setWindowOpacity(0.7)
    window.setFixedSize(window.size())

    btn = QPushButton(window)
    btn.setText("Show System Information in terminal")
    btn.move(250, 25)
    btn.clicked.connect(System_information)
    btn.setStyleSheet("background-color: #4CAF50; color: white;")
    
    sysinfo = QLabel(window)
    sysinfo.setText("Node name: " + platform.node() + "\n" + "System: " + platform.system() + "\n" + "Release: " + platform.release() + "\n" + "Version: " + platform.version() + "\n" + "Machine: " + platform.machine() + "\n" + "Processor: " + platform.processor() + "\n" + "Ip-Address: " + socket.gethostbyname(socket.gethostname()) + "\n" + "Mac-Address: " + ':'.join(re.findall('..', '%012x' % uuid.getnode())))
    sysinfo.move(50, 100)
    sysinfo.setStyleSheet("color: white;")

    bootinfo = QLabel(window)
    bootinfo.setText("Boot Time: " + str(datetime.fromtimestamp(psutil.boot_time())) + "\n" + "Up Time: " + str(datetime.now() - datetime.fromtimestamp(psutil.boot_time())))
    bootinfo.move(500, 100)
    bootinfo.setStyleSheet("color: white;")

    cpuinfo = QLabel(window)
    cpuinfo.setText("Physical cores: " + str(psutil.cpu_count(logical=False)) + "\n" + "Total cores: " + str(psutil.cpu_count(logical=True)) + "\n" + "Max Frequency: " + str(cpufreq.max) + "\n" + "Min Frequency: " + str(cpufreq.min) + "\n" + "Current Frequency: " + str(cpufreq.current))
    cpuinfo.move(50, 250)
    cpuinfo.setStyleSheet("color: white;")

    meminfo = QLabel(window)
    meminfo.setText("Total: " + str(get_size(psutil.virtual_memory().total)) + "\n" + "Available: " + str(get_size(psutil.virtual_memory().available)) + "\n" + "Used: " + str(get_size(psutil.virtual_memory().used)) + "\n" + "Percentage: " + str(psutil.virtual_memory().percent) + "%")
    meminfo.move(500, 150)
    meminfo.setStyleSheet("color: white;")

    swapinfo = QLabel(window)
    swapinfo.setText("Total: " + str(get_size(psutil.swap_memory().total)) + "\n" + "Free: " + str(get_size(psutil.swap_memory().free)) + "\n" + "Used: " + str(get_size(psutil.swap_memory().used)) + "\n" + "Percentage: " + str(psutil.swap_memory().percent) + "%")
    swapinfo.move(325, 220)
    swapinfo.setStyleSheet("color: white;")

    btn = QPushButton(window)
    btn.setText("Show CPU Usage")
    btn.move(500, 240)
    btn.clicked.connect(cpuusage)
    btn.setStyleSheet("background-color: white;")

    btn = QPushButton(window)
    btn.setText("Show CPU Chart")
    btn.move(500, 290)
    btn.clicked.connect(cpuchart)
    btn.setStyleSheet("background-color: white;")

    window.show()
    sys.exit(app.exec_())

def itson():
    print("Show System Information")


if __name__ == "__main__":
    itson()
    window()