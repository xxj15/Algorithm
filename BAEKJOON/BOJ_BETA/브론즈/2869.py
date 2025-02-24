#달팽이는 올라가고 싶다 
import sys , math
input = sys.stdin.readline

a, b, v = map(int, input().split())

days = ((v-b) / (a-b)) 
print(math.ceil(days))