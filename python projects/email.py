

email = input("Enter your Email: ")

k, j, d = 0, 0, 0

# conditions:
#use words before @(at the rate) alse after @(at the rate) use .in, .com, etc.
# for normal email we are using 6 characters.
# uppercase should not be there.
# should contain alphabets.
# at the rate should be used only one time in each email.
# position of dot should be kept on 3rd or 4th from the last.
# space should not be there.
# first letter should be an alphabet. It should not contain a digit and special character.



#explanation:
#Certainly! Let's go through the code step by step:
#1. The code prompts the user to enter an email address using the input() function and stores it in the email variable.
#2. Three variables k, j, and d are initialized to 0. These variables are used to track specific conditions that need to be checked for validating the email.
#3. The code then proceeds to validate the email based on a series of conditions.
#4. Condition 1: if len(email) >= 6 checks if the length of the email is at least 6 characters. This is a minimum length requirement for a valid email address.
#5. Condition 2: if email[0].isalpha() checks if the first character of the email is an alphabet. This ensures that the email starts with a letter.
#6. Condition 3: if "@" in email and email.count("@") == 1 checks if the "@" symbol is present in the email and appears exactly once. This ensures that there is a single "@" symbol in the email.
#7. Condition 4: if (email[-4] == ".") ^ (email[-3] == ".") checks the position of the dot (".") in the email. It uses the XOR operator (^) to ensure that the dot appears either at the 3rd position from the end or at the 4th position from the end. This allows for valid email extensions like ".in" or ".com".
#8. If all the previous conditions are satisfied, the code enters a for loop, where it iterates over each character i in the email.
#9. Inside the loop, the code checks various conditions for each character:
   #- if i.isspace(): checks if the character is a space. If it is, the variable k is set to 1.
   #- elif i.isalpha(): checks if the character is an alphabet. If it is, it further checks if it is an uppercase letter using if i.isupper(). If an uppercase letter is found, the variable j is set to 1.
   #- elif i.isdigit(): checks if the character is a digit. If it is, the code continues to the next iteration of the loop using continue.
   #- elif i == "_" or i == "." or i == "@": checks if the character is one of the allowed special characters in the email (underscore, dot, or @ symbol). If it is, the code continues to the next iteration of the loop using continue.
   #- If none of the above conditions are met, it means that an invalid character is present in the email, and the variable d is set to 1.
#10. After iterating through all the characters in the email, the code checks the values of the variables k, j, and d to determine if any of the invalid conditions were encountered.
#11. If any of the variables k, j, or d are set to 1, it means that an invalid condition was encountered, and the code prints "Wrong Email 5".
#12. If none of the variables k, j, or d are set to 1, it means that all the conditions were satisfied, and the code prints "Correct Email".
#13. If any of the conditions 2, 3, or 4 were not satisfied, the code prints the corresponding error message: "Wrong Email 2", "Wrong Email 3", or "Wrong Email 4".
#14. If the length of the email is less than 6 characters, the code prints "Wrong Email 1" since it does not meet the minimum length requirement.
#This code aims to validate an email address based on the specified conditions and provide appropriate feedback on whether the email is correct or incorrect.
#Code:

if len(email) >= 6:  # 1
    if email[0].isalpha():  # 2
        if "@" in email and email.count("@") == 1:  # 3  # both should be true
            if (email[-4] == ".") ^ (email[-3] == "."):  # using .com
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Correct Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")


#ouputs:
#1st: wcube(Wrong Email 1)
#2nd: ws@cube@gmail.com(Wrong Email 3)
#3rd: wscube@gmail.p(Wrong Email 4)
#4th: ws cube@gmail.com(Wrong Email 5)
#5th: Wscube@gmail.com(Wrong Email 5)
#6th: ws#cube@gmail.com(Wrong Email 5)
#7th: 1wscube@gmail.com(Wrong Email 2)
#8th: ws_cube@gmail.com(Correct Email)
#9th: ws.cube.tech@gmail.com(Correct Email)
 




