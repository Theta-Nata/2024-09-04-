first = int(input('введите 1е число:'))
second = int(input('введите 2е число:'))
third = int(input('введите 3е число:'))
if first==second==third:
    print(3)
elif first==second!=third or first==third!=second or second==third!=first:
    print(2)
else:
    print(0)