list1=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    element=int(input("enter the element"))
    list1.append(element)
    print(list1)
def add_list():
    new=int(input("enter an element to add:"))
    list1.append(new)
    print("element added")
def delete_list():
    global list1
    if not list1:
        print("no elements in the list:")
    else:
        show_list()
        list_index=int(input("enter the index of the element to delete:"))-1
        if 0<=list_index<len(list1):
            del list1[list_index]
            print("element deleted")
        else:
            print("invalid index")
def show_list():
    if not list1:
        print("no element in list")
    else:
        print(list1)
while True:
    print("1.add an element to the list")
    print("2.delete an element from the list")
    print("3.display the list")
    print("4.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        add_list()
    elif choice==2:
        delete_list()
    elif choice==3:
        show_list()
    elif choice==4:
        exit()
    else:
        print("invalid choice")
