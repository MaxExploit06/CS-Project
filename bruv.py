import hashlib
import logging

# Initialize the logger
logging.basicConfig(filename='D:\\Project\\login_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_login_attempt(username, success=True):
    status = "success" if success else "failed"
    logging.info(f"Login attempt: User '{username}' - {status}")

def hash_password(password):
    # You should use a secure hashing algorithm and include a salt in a real application
    return hashlib.md5(password.encode()).hexdigest()

def register_user(username, password):
    with open('D:\\Project\\user_accounts.txt', 'a') as file:
        file.write(f"{username}:{hash_password(password)}\n")

def login(username, password):
    with open('D:\\Project\\user_accounts.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and hash_password(password) == stored_password:
                log_login_attempt(username)
                return True
    log_login_attempt(username, success=False)
    return False


'''username = input('username')
password = input('password')
if username and password:
    register_user(username, password)'''
    

username = input('username')
password = input('password')
if username and password:
    if login(username, password):
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Please enter both username and password")
