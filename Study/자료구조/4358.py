#생태학
import sys
input = sys.stdin.readline
from collections import defaultdict

trees = defaultdict(int) # 기본값이 0
cnt = 0

while True:
    tree = input().strip()
    if not tree :
        break
    trees[tree] += 1 
    cnt += 1

for key, value in sorted(trees.items()):
    percentage = trees[key] / cnt * 100
    print(key, "{:.4f}".format(percentage))