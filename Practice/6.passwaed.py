import random

def generate_password(length=12):
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_-.+=/"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def get_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else:
        return "Strong"
def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length (default is 12): ") or 12)
    password = generate_password(length)
    print(f"Generated password: {password}")
    strength = get_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()


