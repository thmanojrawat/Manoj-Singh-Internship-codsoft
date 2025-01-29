def calculator():
    while True:
        print("-------- My Calculator ---------")

        n1=float(input("Enter First Number:- "))
        n2=float(input("Enter Second Number:- "))

        ch=input("Enter The operation(+,-,*,/) that you want to perform \n and select 0 to stop/exit the app :- ")

        if ch=='+':
            print(f"Sum of {n1} and {n2} is:- {n1+n2}")
        elif ch=='-':
            print(f"Subtraction of {n1} and {n2} is :- {n1-n2}")
        elif ch=='*':
            print(f"Product of {n1} and {n2} is :- {n1*n2}")
        elif ch=='/':
            if n2==0:
                print("division is not possible...")
            else:
                print(f"Division of {n1} and {n2} is :- {n1/n2}")
        elif ch=='0':
            break
        else:
            print("Invalid choice....!!")

calculator()
    