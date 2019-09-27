#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import io
import re
import time
import jieba
import numpy as np
import pandas as pd
import urllib.request
import urllib.parse
import tensorflow as tf
from Data.load_dbdata import upload_data
from global_config import Logger

from run_similarity import BertSim
# 模块导入 https://blog.csdn.net/xiongchengluo1129/article/details/80453599

loginfo = Logger("answer.log", "info")
s= subprocess.Popen(['python','prt.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,err = s.communicate(b'wkdnlkadn')
#print(s.stdout.read())

'''
nextline=s.stdout.readlines()

for line in nextline:
    line = line.decode('gbk')
    #if line.strip() == '输入:':
    print(line.strip())
'''
'''
a = os.system('sh terminal_ner.sh')
print(a)
'''