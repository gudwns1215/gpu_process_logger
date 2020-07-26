import os
import psutil
from time import time, sleep

def detect_gpu_process_status():
    out = os.popen("nvidia-smi | awk '/ C / {print($2\":\"$3\":\"$6)}'").read()
    data = [i.split(":") for i in out.split("\n") if i]
    data = ["# GPU process status", "# TYPE gpu_process_status untyped"] + ["gpu_process_status{"+f"gpu=\"{d[0]}\",pname=\"{psutil.Process(int(d[1])).cmdline()[0]}\""+"} "+f"{d[2][:-3]}" for d in data] + [""]

def write_log(data):
    with open("/run/prometheus/gpu_process_status.prom", "w") as f:
        f.write("\n".join(data))

def process_logging(sleep_duration=5):
    before_data = None
    while True:
        data = detect_gpu_process_status()
        if before_data != data:
            write_log(data)
        before_data = data
        sleep(sleep_duration)
