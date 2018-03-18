import os
import re
import subprocess
import sys
import fcntl
import signal
import getpass


def system(cmd):
          r = os.system(cmd)
          if r!=0:
                 sys.exit(1)


system("""
sudo date --set "2013-7-31 09:30:40"
""")
