import math # import math module

def returnArithmetic():
    # user input
    a = int(input("Please enter a number: "))
    b = int(input("Please enter a second number: "))

    # arithmetic operations
    print("The sum of a and b is ", a + b,"\n"
          "The difference when b is subtracted from a ", a - b,"\n"
          "The product of a and b ", a * b,"\n"
          "The quotient when a is divided by b ", a / b,"\n"
          "The remainder when a is divided by b ", a % b,"\n"
          "The result of log10 a ", math.log10(a), "\n"
          "The result of a^b ", a**b)
    
returnArithmetic()
