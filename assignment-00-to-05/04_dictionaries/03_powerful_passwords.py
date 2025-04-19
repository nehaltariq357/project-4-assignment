


from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email,stored_login,password_to_check):
    if email in stored_login:
        if stored_login[email] == hash_password(password_to_check):
            return True
        else:
            return False
    else:
        return False
    
def main():
    stored_login = {
        "nehal@gmail.com": hash_password("mypassword"),
        "admin@site.com": hash_password("admin123"),
        "user@abc.com": hash_password("qwerty"),
    }

    # User se input lo
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check login
    if login(email, stored_login, password):
        print("Login successful!")
    else:
        print("Login failed. Email or password is incorrect.")
if __name__ == '__main__':
    main()

