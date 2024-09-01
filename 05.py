# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
bmi = weight / height**2
#Write your code below this line 👇
print(int(bmi))
if bmi < 18.5:
  print("You are underweight.")
elif bmi < 25:
  print("You have a normal weight.")
elif bmi < 30:
  print("You are slightly overweight.")
elif bmi >= 30:
  print("You are obese.")
else:
  print("You are clinically obese.")
