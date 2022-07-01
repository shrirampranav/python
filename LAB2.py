# LAB 2: Write a Python program for following conditions. 1. If n is single digit print square of it. 2. If n is two digit print square root of it. 3. If n is three digit print cube root of it.
Number=int(input("Enter the Number:"))
Ans=0
if(Number>0 and Number <=9):
    Ans=Number*Number
    print("The Given Number",Number," is Single Digit Number")
    print("The Square of the Number",Number," is : ",Ans)
elif(Number>9 and Number<=99):
    Ans=Number**(1/2)
    # or Ans=squt(Number)
    print("The Given Number",Number," is Two Digit Number")
    print("The Square root of the Number",Number," is : ",Ans)
elif(Number>99 and Number<=999):
    Ans=Number**(1/3)
    print("The Given Number",Number," is Three Digit Number")
    print("The Cube root of the Number",Number," is : ",Ans)
else:
    print("Enter the Correct Number form 1 to 999")
    
