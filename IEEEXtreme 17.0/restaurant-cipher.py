# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/resaturant_cipher/

# Result: 100%
# Solved by ilyes, IEEEXtreme 17.0

n = int(input())
for i in range(n):
    line = str(input())
    count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for s in line:
        if s in count:
            count[s] += 1
    max_count = max(count.values())  # Move this line outside of the first loop
    for key, value in count.items():
        if value == max_count:
            print(key.upper())
            break
