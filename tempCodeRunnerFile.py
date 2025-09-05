marks=int(input(" Enter your marks :"))
if marks>85 and marks<100:
    print(" congrats you have scored A+grade")
elif marks>65 and marks<=80:
    print("You have scored  A grade")
elif marks>45 and marks<=60:
    print(" you have scored B grade")
elif marks>30 and marks<=40:
    print(" you have scored C grade")
else:
    print(" sorry you are fail")