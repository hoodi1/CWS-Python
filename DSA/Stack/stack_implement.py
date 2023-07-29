stack = []

while True:

    print("/n")
    print("1. Print Stack")
    print("2. Push")
    print("3. Pop")
    print("4. Peak")
    print("5. Check empty")
    print("6. Print size")
    print("7. Exit")
    print()
    choice = int(input("Enter Choice = "))
    if choice == 1:
        if len(stack)==0:
            print("Stack is empty")
        else:
            for i in stack:
                print(i,end=" ")
    
    elif choice == 2:
        n = int(input("Enter number = "))
        stack.append(n)
        print(f"{n} has been added to stack")
    
    elif choice == 3:
        #if len(stack)==0:
        #    print("Stack is empty")
        #else:
        #    p = stack.pop()
        #    print(f"{p} has been removed from stack")
        print("Stack if empty") if len(stack)==0 else print(f"{stack.pop()} has been removed")

    elif choice == 4:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print(stack[-1])
    
    elif choice == 5:
        print("Stack is empty") if len(stack)==0 else print("Stack is not empty")

    elif choice == 6:
        print(f"Size of stack : {len(stack)}")

    elif choice == 7:
        print("exiting")
        break

        