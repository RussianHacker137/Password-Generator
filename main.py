import secrets
import string

x = None
data = string.ascii_letters + string.digits

try:
    x = int(input("Enter the length of the desired password/token: "))
except:
    print("Incorrect input")
if x:
    password = ''.join(secrets.choice(data) for i in range(x))
    print(password)
