
import socket
# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
# getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

with open("login_attempts.txt", "r") as file:
    print(file.read())

username = input("please enter username: ")
password_input = input("Please enter your password: ")


authorised_user = "thanos1"
password = "iaminevitable"
status = ""

# check if credentials are correct

if username != authorised_user or password_input != password:
    print("incorrect credentials")
    status = " Failed login attempt"
else:
    print("welcome", username)
    status = " Successful login"

with open("login_attempts.txt", "a") as file:
    file.write(ip_address)
    file.write(" " + username)
    file.write(status)
    file.write("\n")
