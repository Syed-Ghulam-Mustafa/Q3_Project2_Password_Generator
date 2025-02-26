#project 2: Password Generator 

import random
import string

def generated_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#user inputs
length = int(input("Enter the length of the password: "))
    
password = generated_password(length)
print("Generated Password: ", password)

