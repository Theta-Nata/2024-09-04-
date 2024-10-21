from fake_math import divide as fake_d
from true_math import divide as true_d

result1 = fake_d(12, 4)
result2 = fake_d(12, 0)
result3 = true_d(16, 5)
result4 = true_d(16, 0)

print(result1)
print(result2)
print(result3)
print(result4)