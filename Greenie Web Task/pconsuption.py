import timeit
import psutil
import nvidia_smi 
import subprocess
from os import getpid

platform = psutil.cpu_percent(percpu=True, interval=1) 
mem_usage = psutil.virtual_memory()
print(f"Virtual Memory Used: {mem_usage.used/(1024**3):.2f}G")

my_process = psutil.Process(getpid())
print("Name:", my_process.name()) 
print("PID:", my_process.pid)
print("CPU%:", my_process.cpu_percent(interval=1))

def get_gpu_utilization():
    cmd = "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader"
    utilization = subprocess.check_output(cmd, shell=True)
    utilization = utilization.decode("utf-8").strip().split("\n")
    utilization = [int(x.replace(" %", "")) for x in utilization]
    return utilization

# tuple = (mem_usage, platform)
pc_consumption = ((mem_usage) + (platform)* (utilization)) / 1000 
print(pc_consumption)

maincode="""
for x in range(1,4): #AQUI TENHO QUE POR OS DADOS DO APP
    print(x)
"""

execution_time = timeit.timeit(stmt=maincode, number=1) 
power_consumption = pc_consumption


electricity_consumption = (execution_time * power_consumption) / 1000

print(execution_time) 
print(electricity_consumption) 












