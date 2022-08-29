"""
A+ 90% – 100% 9

Outstanding

A

80% – 89%

8

Excellent

B+

70% – 79%

7

Very Good

B

60% – 69%

6

Good

C+

50% – 59%

5

Above Average

C

40% – 49%

4

Average

D+

30% – 39%

3

Marginal

D

20% – 29%

2

Need Improvement

E

Less Than 20%

1

Need Improvement
"""


print("SASTRA GRADE CALCULATOR")
mark=float(input("Enter your mark: "))
# grade='e'
points=0

if mark>=90 and mark<=100:
    grade='A+'
    points=9
    msg="Outstanding"
#     print(grade)
#     print(points)
elif mark>=80 and mark<=89:
    grade='A'
    points=8
    msg="Excellent"
elif mark>=70 and mark<=79:
    grade='B+'
    points=7
    msg="Very Good"
elif mark>=60 and mark<=69:
    grade='B'
    points=6
    msg="Good"
elif mark>=50 and mark<=59:
    grade='C+'
    points=5
    msg="Above Average"
elif mark>=40 and mark<=49:
    grade='C'
    points=4
    msg="Average"
elif mark>=30 and mark<=39:
    grade='D+'
    points=3
    msg="Marginal"
elif mark>=20 and mark<=29:
    grade='D'
    points=2
    msg="Need Improvement"
elif mark<20:
    grade='E'
    points=1
    msg="Need Improvement"
else:
    print("Pleasee Enter correct Mark!")
print("\n\n")
print("MARK:\t",mark)
print("GRADE:\t",grade)
print("POINTS:\t",points)
print("",msg,"",sep="****")
    