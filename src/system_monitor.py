import psutil
import time

def monitor_system():
    print(f'CPU Usage: {psutil.cpu_percent()}%')
    print(f'Memory Usage: {psutil.virtual_memory().percent}%')

if __name__ == '__main__':
    while True:
        monitor_system()
        time.sleep(5)
