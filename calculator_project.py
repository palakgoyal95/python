number1=input("Enter first number: ")
number2=input("Enter second number: ")
operator=input("Enter operator (+,-,*,/): ")
if operator=="+":
    print(f" The sum of interger:{float(number1)+float(number2)}")
elif operator=="-":
        print(f" The substraction of interger:{float(number1)-float(number2)}")
elif operator=="*":
        print(f" The multiplication of interger:{float(number1)*float(number2)}")
elif operator=="/":
        print(f" The division of interger:{float(number1)/float(number2)}")
else:
        print("Invalid operator")