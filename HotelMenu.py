
menu = {
    "pizza": 250,
    "pasta": 200,
    "burger": 150,
    "fries": 200,
    "coffee": 250
}

print("Welecome to PIY restaurant")
print("pizza: Rs.250\n pasta: Rs. 200\n burger: Rs.150\n fries: Rs.200\n coffee: Rs.250")

Order = input("Do you want to order? (Y/N): ")
item_1 = input("Please enter the name of item you want to order: ")
quntity = int(input("Enter the quantity: "))


total_oreder = 0


if item_1 in menu:
    total_oreder += menu[item_1] * quntity


else:
    print("item not found in menu")

if quntity == 0:
    print("thenks for visitting restaurant")

else:
    print(f"your order of {item_1} is added to your order ☺️")

another_item = input("Do you want to order another item? (Y/N): ")

# for i in range(1, len(menu)):
#     if another_item == "Y":
#         item_2 = input("Enter the name of item you want to order: ")
#         break
#         if item_2 in menu:
#             total_oreder += menu[item_2]
#             print(f"item {item_2} has been added to your order")
#         else:
#             print("item not found in menu")

while another_item == "Y" or another_item == "y":

    item_2 = input("Please enter the name of item you want to order: ")
    quntity = int(input("Enter the quantity: "))

    if item_2 in menu:
        total_oreder += menu[item_2] * quntity
        print(f"item {item_2} has been added to your order ☺️")
    else:
        print("item not found in menu")
    another_item = input("Do you want to order another item? (Y/N): ")


print("The total cost of your order is: ", total_oreder)
