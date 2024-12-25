import re

with open("input") as f:
    text = f.read()

# regex = re.findall(r"mul\((\d+),(\d+)\)", text)

# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
regex = re.split(r"(do\(\)|don't\(\))", text)
# print(sum(int(x) * int(y) for x, y in regex))

on = True

s = 0

for i in regex:
    if i == "don't()":
        on = False
    elif i == "do()":
        on = True

    if on:
        regex = re.findall(r"mul\((\d+),(\d+)\)", i)
        s += sum(int(x) * int(y) for x, y in regex)

print(s)

# s1 = 0
# regex = re.findall(r"do\(\)((?!.*do\(\)))don't\(\)", text)
# for t in regex:
#     print(t)
#     s1 += sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", t))

# print(s1)
