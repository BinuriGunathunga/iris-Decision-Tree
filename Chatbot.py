question = input("What is your symptom? ").lower()
if "headache" in question:
    print("Try relaxinng or taking mild pain relife.")
elif "fever" in question:
    print("You might need resst and hydration. ")
elif "cough" in question:
    print("Consider using cough syrup or seeing a doctor if it persists.")
elif "stomach ache" in question:
    print("Avoid solid food for a few hours and try drinking clear fluids.")
else:
    print("I'm sorry, I don't have advice for that symptom.")