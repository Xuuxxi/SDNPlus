import re

# 按前端要求处理成json返回
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

    info1 = []
    info2 = []
    info3 = []

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
