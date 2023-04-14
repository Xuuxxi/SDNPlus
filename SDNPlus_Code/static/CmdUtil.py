import time

import paramiko


def connect_and_work(src, dst, num):
    # 创建ssh链接
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # ssh认证
    ssh_client.connect('192.168.238.132', username='p4', password='p4')

    # 创建四个终端窗口
    channel1 = ssh_client.invoke_shell()
    channel2 = ssh_client.invoke_shell()
    channel3 = ssh_client.invoke_shell()
    channel4 = ssh_client.invoke_shell()

    # make 编译
    cmd1 = 'cd tutorials/exercises/final/ \n ls \n make stop \n make \n'
    channel1.send(cmd1.encode('utf-8'))
    # 等待该步骤执行完成
    time.sleep(10)

    # 运行 mycontroller.py
    cmd2 = 'cd tutorials/exercises/final/ \n ./mycontroller.py\n'
    channel2.send(cmd2.encode('utf-8'))
    # 等待该步骤执行完成
    time.sleep(1)

    # src 发出 num 数量的包
    cmd3 = 'cd tutorials/exercises/final/ \n mx h1 \n ./send.py ' + src + ' ' + num + '\n'
    channel3.send(cmd3.encode('utf-8'))

    # dst 接受包
    cmd4 = 'cd tutorials/exercises/final/ \n mx ' + dst + ' \n ./receive.py\n'
    channel4.send(cmd4.encode('utf-8'))
    # 根据发包数量进行等待，这边的发包和收包是同时进行的
    time.sleep(int(num))

    # 接受结果返回
    res = ''
    while channel4.recv_ready():
        res += channel4.recv(1024).decode('utf-8')

    ssh_client.close()
    return res
