# Дано
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Считаем средний бал в списке
s_b1 = sum(grades[0])/len(grades[0])
s_b2 = sum(grades[1])/len(grades[1])
s_b3 = sum(grades[2])/len(grades[2])
s_b4 = sum(grades[3])/len(grades[1])
s_b5 = sum(grades[4])/len(grades[4])
print(s_b1,s_b2, s_b3, s_b4, s_b5)
# упорядочиваем список по алфавиту
S_students = sorted(students)
print(S_students)
s_b_students = {S_students[0]:s_b1,S_students[1]:s_b2, S_students[2]:s_b3, S_students[3]:s_b4, S_students[4]:s_b5}
print ('средний балл учащихся: ', s_b_students )
