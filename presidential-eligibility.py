"""
San Kwon

codehs 4.4.5: Presidential Eligibility

This program asks the user to input their age, whether or not
they are born in the US, and the years of their residency in the US.
Based on this information, the program determines and prints whether or
not the user is eligible to run for president.
"""

# ask user for age
age = int(input("Age: "))

# ask user whether they were born in the U.S.
citizen = input("Born in the U.S.? (Yes/No): ")

# ask user for years of residency
residency = int(input("Years of Residency: "))

# detrmine and print whether the user is eligible to run for president
if age >= 35 and citizen == "Yes" and residency >= 14:
    print ("You are eligible to run for president!")
else:
    print ("You are not eligible to run for president.")
