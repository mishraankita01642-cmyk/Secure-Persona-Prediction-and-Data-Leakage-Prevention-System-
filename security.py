import bcrypt

# 1. Hash password
def hash_password(password):
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    return hashed_password.decode("utf-8")

# 2. Verify password during login
def verify_password(password, stored_hash):
    password_bytes = password.encode("utf-8")
    stored_hash_bytes = stored_hash.encode("utf-8")

    return bcrypt.checkpw(
        password_bytes,
        stored_hash_bytes
    )

# 3. Check password strength
def check_password_strength(password):

    if len(password) < 8:
        return "Weak"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if has_upper and has_lower and has_digit:
        return "Strong"

    return "Medium"

# Testing
if __name__ == "__main__":

    password = input("Enter password: ")

    # Hash the password
    hashed = hash_password(password)

    print("\nOriginal Password:", password)
    print("Hashed Password:", hashed)

    # Check strength
    print("Password Strength:",
          check_password_strength(password))

    # Test correct password
    test_password = input("\nEnter password again to verify: ")

    if verify_password(test_password, hashed):
        print("Password verified successfully!")
    else:
        print("Incorrect password!")
