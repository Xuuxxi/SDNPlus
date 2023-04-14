import re


def getinfo(info_str):
    temp = info_str.split('\n')
    s = []

    temp_s = ''
    for i in range(5, len(temp)):
        if temp[i] == '':
            continue

        temp_s += '&' + temp[i]
        if i + 1 < len(temp) and temp[i + 1] == '':
            s.append(temp_s)
            temp_s = ''

    #
    info1 = []
    #
    info2 = []
    #
    info3 = []

    # 三种类型信息
    # 1 &Received from ('10.0.2.2', '10.0.1.1', 6, 42038, 20) total: 1
    # 2 &Switch 1 - Port 1: 0.0002468473795190896 Mbps&Switch 4 - Port 2: 0.0002143781265709897 Mbps&Switch 2 - Port 3: 0.00015830106974646196 Mbps&Switch 3 - Port 2: 0.0001486917086112064 Mbps&Switch 1 - Port 3: 0.00010678931122423795 Mbps&Switch 3 - Port 1: 0.0001017597091237853 Mbps&Switch 2 - Port 4: 7.198656370788392e-05 Mbps&Switch 4 - Port 1: 6.0076307638613117e-05 Mbps&Switch 1 - Port 4: 2.6709910754119552e-05 Mbps&Received from ('10.0.2.2', '10.0.1.1', 6, 42038, 20) total: 2
    # 3 &Switch 1 - Port 1: 0.0012151711953794562 Mbps&Switch 4 - Port 2: 0.0010855494372783105 Mbps&Switch 2 - Port 3: 0.0009555964378694905 Mbps&Switch 3 - Port 2: 0.0008255029729874066 Mbps&Switch 1 - Port 3: 0.0006952824901976938 Mbps&Switch 3 - Port 1: 0.0005650571894019178 Mbps&Switch 2 - Port 4: 0.0004347058264165297 Mbps&Switch 4 - Port 1: 0.00030439442269695273 Mbps&Switch 1 - Port 4: 0.00017396488627498594 Mbps

    # 提取元组和数字
    match = re.search(r"\((.*?)\)(.*?):\s*(\d+)", s[0])
    if match:
        # 解析元组
        arr = match.group(1).split(", ")
        arr = [x.strip("'") for x in arr]

        temp_info = {}
        temp_info['s1'] = arr[0]
        temp_info['s2'] = arr[1]
        temp_info['s3'] = arr[2]
        info1.append(temp_info)

    for i in s:
        pattern = r"Received from \('.*?', '.*?', \d+, \d+, \d+\) total: \d+"
        result = re.findall(pattern, i)
        if result:
            info2.append({'s1': result[0]})

    for i in s:
        pattern = r"(Switch \d+ - Port \d+): (\d+\.\d+) Mbps"
        result = re.findall(pattern, i)
        if result:
            for j in result:
                info3.append({j[0]: j[1]})

            info3.append({'newLine': 'none'})

    info = [info1, info2, info3]

    return info
