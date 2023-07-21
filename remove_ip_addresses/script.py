import_file = "allowed_ip_addresses.txt"

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# read file and store in variable as a list
with open(import_file, "r") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()
flagged_addresses = []

# Loop through `remove_list` and remove bad ip addresses from ip_addresses variable
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
        flagged_addresses.append(element)
        print("Will remove ", element, "from ", import_file)


# Convert `ip_addresses` back to a string so that it can be written into the text file
ip_addresses = "\n".join(ip_addresses)

# rewrite original file if any addresses are flagged.

if len(flagged_addresses) > 0:
    # Rewrite the original file
    with open(import_file, "w") as file:
        file.write(ip_addresses)
        print("Succesfully removed ", remove_list, "from file")
else:
    print("no unwanted ip_addresses in list")


# use original_list.txt to reset import_file
def reset():
    with open("original_list.txt", "r") as reset_file:
        with open(import_file, "w") as file:
            file.write(reset_file.read())
            print("File reset")


reset_request = input("Reset file? (y/n): ").lower().strip()

if reset_request[:1] == "y":
    reset()
