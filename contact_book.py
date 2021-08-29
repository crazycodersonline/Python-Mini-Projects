names = []
phone_numbers = []

num = 3

for i in range(num):
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    
    names.append(name)
    phone_numbers.append(phone_number)
    
    
print("\tName\t\t\tPhone Number")

for i in range(num):
    print(f'\t{names[i]}\t\t\t{phone_numbers[i]}')
    
s = input("Enter the Name to search: ")
if s in names:
    index = names.index(s)
    name = names[index]
    phone_number = phone_numbers[index]
    
    print(f"Name:{name} , Phone Number:{phone_number}")
else:
    print("Name not found!")
    
    