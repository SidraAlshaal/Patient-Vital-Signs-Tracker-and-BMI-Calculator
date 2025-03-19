#Challenge: Medical Patient records Analysis.
#Create a system to track a patient vital signs and calculate their body mass index(BMI).
#The system should store patient records in JSON file & provide basic Analysis.
#This project was done by: Sidra Alshaal

import os
import json
import math

#Opening the json file 
with open("BMI.json","r") as file:
    patients=json.load(file)

#Recieving the patients data
name=input("Enter the patient's name: ")

age=int(input("Enter the patient's age: "))
if age<0 :
   print("Invalid input, Try again.")

weight=float(input("Enter the patient's weight in kilograms: "))
if weight<0 : 
   print("Invalid input, Try again.")

height=float(input("Enter the patient's height in meters: "))
if height<0:
   print("Invalid input, Try again.")

#JSON file format
newpatient={"name":name,"age": age, "weight": weight, "height": height}
patients.append(newpatient)

#BMI Calculation function
h=height**2
BMI=(weight/h)
print(f"BMI: {BMI:2f}")

#BMI Category Classification
if 18.5 <= BMI < 25:
    print("You have normal weight. ")
elif BMI<18.5:
    print("You are underweight. ")
elif 24.9<= BMI<29.9:
    print("You are overweight. ")
elif BMI>29.9:
    print("You are obese. ")
else:
    print("Error")

#Saving the new patients data in the JSON file
with open("BMI.json","w") as file:
    json.dump(patients,file)