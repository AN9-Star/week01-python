import sys
import os

if len(sys.argv) < 2:
    print("用法：python wordcount.py 文件名")
    sys.exit()

path = sys.argv[1]
if not os.path.exists(path):
    print("找不到文件：" + path)
    sys.exit()

def count_words(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
        words = text.lower()
        words1 = words.split()

    counts = {}

    for word in words1:
        word = word.strip(".,!?;:\"'()")    # ← 每轮先擦标点
        if not word:                         # ← 擦完是空的就跳过
            continue
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts 
counts = count_words(path)
t = counts.items()
t1 = sorted(t, key=lambda p: p[1], reverse=True)[:10]
for word, n in t1:
    print(word, n)


    
