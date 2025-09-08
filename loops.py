num1 = int(input("enter number"))
for i in range(1,11):
    print(f"{num1} X {i}={num1*i}")

row = int(input("enter amount of rows"))
for i in range(1,row+1):
    for j in range(i):
        print("*", end=(" "))
    print()

num2 = int(input("enter a number"))
for i in range(2, int (num2** .5)+1):
    if num2 %i ==0:
        print(f"{num2} is not a prime number")
        break
else:
    print(f"{num2} is a prime number")
    
    
