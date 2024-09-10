# 讀取文件並替換每行的第一個空格為 \t
with open('pronDictOriginal.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 替換每行的第一個空格為 \t
with open('output.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        # 使用一次性替換每行的第一個空格
        file.write(line.replace(' ', '\t', 1))
