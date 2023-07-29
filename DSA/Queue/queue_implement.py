#queue - first in first out 

queue = []

while True:

    print()
    print("1. Enque")
    print("2. Deque")
    print("3. Display")
    print("4. Front")
    print("5. Rear")
    print("6. Size")
    print("7. Empty")
    print("8. Exit")
    print()
    choice = int(input("Enter Choice = "))
    if choice == 3:
        if len(queue)==0:
            print("queue is empty")
        else:
            for i in queue:
                print(i,end=" ")
    
    elif choice == 1:
        n = int(input("Enter number = "))
        queue.append(n)
        print(f"{n} has been added to queue")
    
    elif choice == 2:
        print("queue if empty") if len(queue)==0 else print(f"{queue.pop(0)} has been removed")

    elif choice == 4:
        if len(queue)==0:
            print("queue is empty")
        else:
            print(f"Front of queue is : {queue[0]}")
    
    elif choice == 5:
        print("queue is empty") if len(queue)==0 else print(f"Rear of queue is: {queue[-1]}")

    elif choice == 6:
        print(f"Size of queue : {len(queue)}")

    elif choice == 7:
        print("queue is empty") if len(queue)==0 else print("Queue is not empty")

    elif choice == 8:
        print("exiting")
        break

        