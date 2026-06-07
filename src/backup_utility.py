import shutil
import os
from datetime import datetime

def backup(source, destination):
    today = datetime.now().strftime('%Y-%m-%d')
    dest = os.path.join(destination, f'backup_{today}')
    shutil.copytree(source, dest)
    print(f'Backup created at {dest}')
