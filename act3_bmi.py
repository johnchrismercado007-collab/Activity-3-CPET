weight = float(input("please enter your weight (kg);"))
height = float(input("please enter your height (m);"))

bmi = weight / (height**2)

ight (m);"))

bmi = weight / (height**2)

g
if bmi <= 18.5:
    print("underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
