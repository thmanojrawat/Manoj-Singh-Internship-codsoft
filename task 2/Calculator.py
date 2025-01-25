print("-------- My Calculator ---------")

n1=float(input("Enter First Number:- "))
n2=float(input("Enter Second Number:- "))

ch=input("Enter The operation(+,-,*,/) that you wan to perform:- ")

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
else:
    print("Invalid choice....!!")
