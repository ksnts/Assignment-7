#password rules
print("Input your desired password:\nNote that password must be:\n")
print("1. Greater than 15 letters\n2. Have at least one capital letter\n3. Have at least one number\n4. Have at least one special char (!@#$%^&*()_+ etc)")
#variables
char1=False
caseU=False
num1=False
char2=False
x=1
#loop for continuous trial
while x == 1:
    #user password input
    pass1=input("\nPassword: ")
    #if statement to determine length of password
    if len(pass1) >15:        
        char1=True
#for loop for uppercase
    for index in pass1:
        if index in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            caseU=True
#for loop for numbers            
    for index in pass1:
        if index in '1234567890':
            num1=True
#for loop for special char                    
    for index in pass1:
        if index in '~.,<>:;[]=-`?!@#$%^&*()_+':
            char2=True
            
    print("\n")
#if else for checking requirements
    if char1==True:
        print("More than 15 letters: ✓")
    else:
        print("More than 15 letters: X")
    
    if caseU==True:
        print("Upper case: ✓")
    else:
        print("Upper case: X")
    
    if num1==True:
        print("Number: ✓")
    else:
        print("Number: X")

    if char2==True:
        print("Special character: ✓")
    else:
        print("Special character: X")
#if statement for password validation
    if char1==True and caseU==True and num1==True and char2==True:
        x=0
        print("\nPassword is Valid!")
#else statement to reset and retry 
    else:
        x=1
        char1=False
        caseU=False
        num1=False
        char2=False
        print("\nPassword is invalid!\nTry again")
    







        
    
    

