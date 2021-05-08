
import glob
import gpiozero
import time
import re

class DS18S20:
    def __init__(self):
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.dev_file = device_folder + '/w1_slave'
    
    def get(self):
        while True:
            with open(self.dev_file, 'r') as F:
                lines = F.readlines() 
            if "YES" not in lines[0]:
                time.sleep(0.2)
                continue
            m = re.search(r" t=(\d+)$", lines[1])
            if m:
                return int(m.group(1)) / 1000
            Exception("boom")

def transform(val, off, fact, min_, max_):
    x = (val - off) * fact
    x = min(x, max_)
    x = max(x, min_)
    return x

sensor = DS18S20()
while True:
    cpu_temp = gpiozero.CPUTemperature().temperature
    hdd_temp = sensor.get()

    print("cpu: %s, hdd: %s" % (cpu_temp, hdd_temp))

    time.sleep(10)    
    