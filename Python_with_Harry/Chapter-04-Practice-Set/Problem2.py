# To accepts marks of 6 students and print them in sorted order

marks = []

f1 = int(input("Please enter your marks : "))
marks.append(f1)
f2 = int(input("Please enter your marks : "))
marks.append(f2)
f3 = int(input("Please enter your marks : "))
marks.append(f3)
f4 = int(input("Please enter your marks : "))
marks.append(f4)
f5 = int(input("Please enter your marks : "))
marks.append(f5)
f6 = int(input("Please enter your marks : "))
marks.append(f6)

marks.sort()

print(marks)