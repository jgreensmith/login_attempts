
import socket
# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
# getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

# read file and check how many failed logins there are
with open("login_attempts.txt", "r") as file:
    failed_attempts = file.read().count("Failed")


# hard coded credentials
authorised_user = "thanos1"
password = "iaminevitable"
status = ""

# lock access if reach 3 failed login attempts
if failed_attempts >= 3:
    print("you've been locked out!")
else:
    # login form
    username = input("please enter username: ")
    password_input = input("Please enter your password: ")

    # check if credentials are correct
    if username != authorised_user or password_input != password:
        print("incorrect credentials")
        status = " Failed login attempt"
    else:
        print("welcome", username)
        status = " Successful login"

    # append file with new authorisation log entry
    with open("login_attempts.txt", "a") as file:
        file.write(ip_address)
        file.write(" " + username)
        file.write(status)
        file.write("\n")
