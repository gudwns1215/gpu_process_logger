import os
import psutil
import pwd
from time import time, sleep

def detect_gpu_process_status():
    data = os.popen("nvidia-smi | awk '/ C /'").read().split("\n")
    data = [i[1:-1].replace("  ", " ") for i in data]
    while any(["  " in d for d in data]):
        data = [i.replace("  ", " ") for i in data]
    data = [i.split(" ") for i in data]
    data = [[i[1], i[2], i[-2]] for i in data if len(i)>3]

    new_data = []
    for d in data:
        try:
            ps = psutil.Process(int(d[1]))
        except psutil.NoSuchProcess as e:
            print(f"Process {d[1]} doesn't exist.")
            continue
        username = ps.username()
        if username.isnumeric():
            username = pwd.getpwuid(int()).pw_name
            
        new_data.append(
            "gpu_process_status{"+f"gpu=\"{d[0]}\",pid=\"{int(d[1])}\",pname=\"{' '.join(ps.cmdline()).strip()}\",username=\"{username}\""""+"} "+f"{d[2][:-3]}"
        )

    data = ["# GPU process status", "# TYPE gpu_process_status untyped"] + new_data + [""]
    return data

def write_log(data):
    with open("/run/prometheus/gpu_process_status.prom", "w") as f:
        f.write("\n".join(data))
    

def process_logging(sleep_duration=5):
    before_data = None
    while True:
        data = detect_gpu_process_status()
        if before_data != data:
            print(data)
            write_log(data)
        before_data = data
        sleep(sleep_duration)

if __name__=="__main__":
    process_logging()
