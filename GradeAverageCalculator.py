#quiz

GradeOne = int(input("Enter your Grade: "))
GradeTwo = int(input("Enter your Grade: "))
GradeThree = int(input("Enter your Grade: "))
GradeFour = int(input("Enter your Grade: "))
GradeFive = int(input("Enter your Grade: "))
GradeSix = int(input("Enter your Grade: "))
GradeSeven = int(input("Enter your Grade: "))
GradeEight = int(input("Enter your Grade: "))

totalGrade = (GradeOne + GradeTwo + GradeThree + GradeFour + GradeFive + GradeSix + GradeSeven + GradeEight )
AverageGrade = (totalGrade // 8)
print(AverageGrade)
if AverageGrade >= 100 and AverageGrade <= 50:
    print("Invalid Grade")
elif AverageGrade >=98 :
    print("With Highest Honor")
elif AverageGrade >=94 :
    print("With High Honor")
elif AverageGrade >=90 :
    print("With Honor")
elif AverageGrade >=75 :
    print("Passed")
elif AverageGrade <=74 :
    print("Failed")

