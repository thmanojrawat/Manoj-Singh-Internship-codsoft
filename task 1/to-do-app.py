def task():
    tasks=[]           
    print("\n-----WELCOME TO-DO LIST APP-----\n")

    total_tasks = int(input("Enter the number of task you want to add:- "))
    for i in range(total_tasks):
        task=input(f"Enter task {i+1} :- ")
        tasks.append(task)
    
    print("\nYour Today's Tasks are:- ")
    for m in tasks:
        print(m)

    while True:
        op=int(input("Enter 1 to add\n2 to update\n3 to delete\n4 to view\n5 to Exit or Stop:- "))
        
        if op==1:
            add=input("Enter the task You want to add:- ")
            tasks.append(add)
            print(f"Task {add} is succesfully added.....")
        elif op==2:
            val=int(input("Enter the task number You want to update:- "))
            for i in range(1,len(tasks)+1):
                if val==i:
                    update_task=input("Enter the Task that you want to update:- ")
                    tasks[i-1]=update_task
                    print(f"Task {update_task} is successfully added...")
                else:
                    flag=0
            if flag==0:
                print(f"Task {val} Not Found...")  

        elif op==3:
            val=int(input("Enter the task number You want to delete:- "))
            for i in range(1,len(tasks)+1):
                if val==i:
                    del tasks[i-1]                 
                    print(f"Task {val} is successfully deleted...")
                else:
                    flag=0
            if flag==0:
                print(f"Task {val} Not Found...") 

        elif op==4:
            print("Displaying All the Tasks : ")
            for m in tasks:
                print(m)
        elif op==5:
            print("Closing the app...")
            break
        else:
            print("Invalid Choice...")

task()
        
                


