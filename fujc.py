#coding=utf-8
import os
from subprocess import PIPE, Popen

# 这几行是获取 子程序 可执行文件的位置，没有啥意义
cur_file = os.path.realpath(__file__)
cur_path = os.path.dirname(cur_file)
exec_file = cur_path + '/' + 'subpcs.py'
# 假设目的程序是 B.py
# 注意：代码在 Unix 类操作系统上正常，对于 Windows 不知道，可能结果错误

# 下面这行是创建子进程，在终端里就是 python B.py。 输入输出是管道。
p = Popen("python " + exec_file, shell=True, stdout=PIPE, stdin=PIPE)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# 假设下面是程序里用户交互部分：
while True:
    some_str = "可能是用户输的字符串，作为标准输入。\n"
    # 注意结尾一定要有换行符，因为标准输入是通过换行符结束的
    # 因此弊端就是 如果输入中就有换行符，需要自己处理，比如
    # 替换为 ||换行||，再在子程序里处理

    # 转 utf8
    p.stdin.write(bytes(some_str, encoding='utf8'))
    p.stdin.flush()
    # 至此，some_str 已经被传输到了 B 的标准输入流
    # 参照下面 B.py 看
    out_bytes = p.stdout.readline()
    # 至此，B 的标准输出流的一行 被读到 out_bytes

    print(str(out_bytes, encoding='utf8'))

    import time

    time.sleep(1)
