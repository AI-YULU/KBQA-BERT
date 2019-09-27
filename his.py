#!/usr/bin/python

import os
import sys
import subprocess


# call mib2c
def callmib():
    exestr = 'python zijc.py'
    p = subprocess.Popen(exestr, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        line = p.stdout.readline()
        print
        line
        if not line:
            break
        if line.startswith('this is opt1'):
            opt = 'aaa'
        elif line.startswith('this is opt2'):
            opt = 'bbb'

        p.stdin.write(opt + os.linesep)

    p.wait()
    errout = p.stderr.read()
    p.stdout.close()
    p.stderr.close()
    p.stdin.close()
    print


# main funciton
# Step 1. make C files first time
callmib()