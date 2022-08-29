import secrets
import string

x = None
try:
    x = int(input("Enter the length of the desired password/token: "))
except:
    print("Incorrect input")
if x:
    data = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(data) for i in range(x))
    print(password)