#This python program shows the grade of student based on the 5 subject marks.

m1=int(input("Enter marks of Maths :"))
m2=int(input("Enter marks of English :"))
m3=int(input("Enter marks of Science :"))
m4=int(input("Enter marks of Geography :"))
m5=int(input("Enter marks of History :"))
per=(m1+m2+m3+m4+m5)/5
print("Percentage =",per)
if per > 90:
    print("A Grade")
elif per > 75:
    print("B Grade")
elif per>=35:
    print("C Grade")
else:
    print("Fail")
