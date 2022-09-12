





# Name: Aayusha Kattel                Date Assigned: Aug 31, 2022

# Course: 2000-Sec 44306              Due Date: Sept 8, 2022

# File name: computer assignment 1.py

# Program Description: > Asks the user for email and phone number
#                      > Prints the domain of email
#                      > Prints the phone number in specific format


print("="*33) #=======
print(" "*12+"YOUR INFO") # heading
print("="*33) #=======

print(" ") #spacing




# asking email to the user
email = input("Enter email: ")

# asking phone no to the user
phoneNo = input("Enter phone number: ")



print(" ") # spacing

print("="*33) #========

print(" ") # spacing



# assigning all the characters after @ to variable "domain"
domain = email[email.find('@')+1:]


# it capitalizes the first  letter and print the "domain" i.e Gmail.com
print("Domain:   ",domain.capitalize())







print(" ") # spacing


# assigning username to variable "userName"
userName = email[0:email.find('@')]

# printing the variable "usweName"
print("User Name:"  , userName)




print(" ") # spacing




# formatting the phoneNo in specific format i.e (000) 000-0000
numberFormat = '('+phoneNo[:3]+')'+" "+phoneNo[3:6]+"-"+phoneNo[6:]

#printing phone number
print("Phone:    ", numberFormat)









































