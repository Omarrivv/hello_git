print("Login V2 Modificado Arreglado")

username = input("### Enter your username: ")
password = input("### Enter your password: ")

usernameAdmin = "admin"
passwordAdmin = "admin123"

if username == usernameAdmin and password == passwordAdmin:
    print("Welcome, Admin!")
elif username and password:
    print(f"Welcome, {username}!")
else:
    print("Please enter both username and password.") # a español dice "por favor ingrese ambos nombres de usuario y contraseña."

# This code prompts the user for a username and password, and then greets them if both are provided.
# If either is missing, it asks them to enter both.
