"""A fully fledged out example on using subprocess 
can be found at: https://github.com/KonScanner/wifi-swap"""
import subprocess

# This is a simple way to execute commands, and act on the output.
result = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
for i in result.stdout.readlines():
    print(i)
