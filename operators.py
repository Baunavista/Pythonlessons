#  arithmetic operators
a = 5
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
x = 3
# x = x + 3
x+=3
print(x)

# comparison operators
age1 = 23
age2 = 45
age3 = age1>age2
print(age3)

age4 = 56
age5 = 23
age6 = age4<age5
print(age6)

marks1 = 200
marks2 = 200
marks3 = marks1>=marks2
print(marks3)

marks4 = 242
marks5 = 147
marks6 = marks4<=marks5
print(marks6)

marks7 = 15
marks8 = 8
print(marks7==marks8)

marks9 = 65
marks10 = 91
print(marks9!=marks10)

c = 4
d = 8
e = 5
f = 9

print(c + d > e + f)
print(c + d < e + f)
print(c + d >= e + f)
print(c + d <= e + f)
print(c + d == e + f)
print(c + d != e + f)

logical operators
student1 = 23
student2 = 67
student3 = 45
student4 = 35
print(student1>student2 and student3>student4)
print(student1<student2 and student3<student4)
print(student1>student2 and student3<student4)
print(student1<student2 and student3>student4)
print(student1>student2 or student3>student4)
print(student1<student2 or student3<student4)
print(student1>student2 or student3<student4)
print(student1<student2 or student3>student4)
print(not(student1<student2 or student3>student4))

age1 = input("What is the age of the first student? ")
age2 = input("What is the age of the second student? ")
age3 = input("What is the age of the third student? ")
age4 = input("What is the age of the fourth student? ")

print(age1>age2 and age3>age4)
print(age1==age2 and age3!=age4)
print(age1<=age2 or age3>=age4)
print(age1<age2 or age3<age4)
