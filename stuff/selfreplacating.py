import time
import subprocess
from sys import argv
strr = int(round(time.time()))
strr = str(strr) + '.py'
subprocess.call(['cp',argv[0],strr])
