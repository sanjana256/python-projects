import random

def generate_password(length):
    lowers="abcdefghijklmnopqrstuvwxyz"    
    uppers=lowers.upper()
    numbers="0123456789"
    symbols="!@#$%^&*"
    characters = lowers + uppers + numbers + symbols
    password = ''.join(random.choice(characters) for _ in range(length))
    return(password)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password does'nt exist")
            return
        
        password = generate_password(length)
        print(f"Password: {password}")
    
    except ValueError:
        print("Invalid input.")
    
main()
