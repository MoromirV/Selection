#test grading program

testScore = int(input("Please enter your test score: "))
if testScore <= 25:
    print("Fail")
elif testScore <= 40:
    print("E grade")
elif testScore <= 50:
    print("D grade")
elif testScore <= 60:
    print("C grade")
elif testScore <= 70:
    print("B grade")
elif testScore <= 80:
    print("A grade")
elif testScore <=95:
    print("A* grade")
elif testScore <=100:
    print("A** grade")
