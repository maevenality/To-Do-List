#Josi Johnson
#Initialize
todolist= []

def add():
    item = input("what item do you want to add? ")
    todolist.append(item)

def remove():
    item = input("what item do you want to remove? ")
    todolist.remove(item)

def complete():
    item = input("what item do you want to mark as done? ")

    i = todolist.index(item) 
    todolist[i] = "✓"

def view():
    print(todolist)

def removeAll(): 
    todolist.clear()

def sort(): 
    todolist.sort()

def printNum():
    print("Number of items in the list = ", len(todolist))

while True:
    print("select option \n1. add item \n2. remove item \n3. complete item \n4. view list \n5. remove all items from the list \n6. sort list \n7. view number of items \n8. exit program")
    option = int(input("option:"))
    if (option == 1):
        add()

    if (option == 2):
        remove()

    if (option == 3):
        complete()

    if (option == 4):
        view()

    if (option == 5): 
        removeAll()

    if (option == 6):
        sort()

    if (option == 7):
        printNum()

    if (option == 8):
        quit()
        break

#main