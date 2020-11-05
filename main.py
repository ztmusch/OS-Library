import os

while True:
    directory = input("Hello! Please enter the name of the directory you would like to save the file in: ")
    print(directory)

    if os.path.isdir(directory):
        break

    else:
        print("The directory entered does not exist. Please try again.")

file_name = input("Please enter the name of the file: ")
print(file_name)
print("Thank you for the information!")
user_name = input("Please enter your name: ")
print(user_name)
user_address = input("Please enter your address: ")
print(user_address)
user_phone_number = input("Please enter your phone number: ")
print(user_phone_number)

cs_string = user_name + "," + user_address + "," + user_phone_number + "\n"

write_file = open(os.path.join(directory, file_name), 'a')
write_file.write(cs_string)
write_file.close()

print("File contents:", )

read_file = open(os.path.join(directory, file_name), 'r')
for line in read_file:
    print(line.rstrip())
read_file.close()
