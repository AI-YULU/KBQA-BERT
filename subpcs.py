#coding=utf-8
import sys

while True:
    # 这里的 txt，就是 A write 的数据，标准输入
    txt = input()

    # 这里是业务处理
    v = txt + ' from B'

    # 标准输出，在别的可执行程序里可能是 echo 等，结果都流到了 A 中
    print(v)
    sys.stdout.flush()
