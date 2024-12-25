import sys

sys.path.append("/".join(__file__.split("/")[:-2]))
import utils

list1 = []
list2 = []

for x, y in utils.input_lines("{int}  {int}"):
    list1.append(x)
    list2.append(y)

assert len(list1) == len(list2)
list1.sort()
list2.sort()

dist = 0
for i in range(len(list1)):
    dist += abs(list1[i] - list2[i])

print(dist)
