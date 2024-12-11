"""
    This is a docString it
    is multiline
"""
the_list = []
def save_list():
    global the_list
    with open("data.txt", "w") as file:
        file.writelines(item + "\n" for item in the_list)

def load_list():
    global the_list
    with open("data.txt", "r") as file:
        the_list = [line.strip() for line in file]
the_list = ["Red", "Blue", "Green", "Yellow"]
save_list()
the_list = []
print(the_list)
load_list()
print(the_list)
"""
# This is how you create a list
myList = ["red", "orange", "blue"] # comment
# print the list
print(myList)
# access individual items in the list using the index
print(myList[1])
# add an item to the list
myList.append("green")
print(myList)
# this will remove the 2nd item in the list
myList.pop(1)

# how to make a menu
# repeat until 3 is pressed
while True:
    print("Press 1 for fun")
    print("Press 2 for work")
    print("press 3 to quit")
    choice = input()
    if choice == "1":
        print("You choose fun")
    elif choice == "2":
        print("You choose work")
    elif choice == "3":
        print("Bye!!")
        break
    else:
        print("Invalid choice")

list2 = ["a1", "a2", "a3", "a4", "a5"]

for c in range(0, len(list2)):
    print(str(c+1) + ". " + list2[c] )
while True:
    choice = input("Which one to remove or q to quit?")
    if choice == "q":
        break
    if choice.isdigit():
        choice = int(choice) - 1
        if choice >= len(list2) or choice < 0:
            print("Invalid choice")
        else:
            list2.pop(choice)
    else:
        print("Invalid choice")

print(list2)"""