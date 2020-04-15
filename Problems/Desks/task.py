# put your python code here
group1 = int(input())
group2 = int(input())
group3 = int(input())

class1 = group1 + (group1 % 2)
class2 = group2 + (group2 % 2)
class3 = group3 + (group3 % 2)
import math
desks_needed = math.ceil(class1 + class2 + class3) / 2

print(math.ceil(desks_needed))
