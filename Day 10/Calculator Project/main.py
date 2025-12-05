def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

dict_operations={"+":add,
                "-":subtract,
                "*":multiply,
                 "/":divide
                 }

print(dict_operations["*"](2,3))
while 5>4:
    keep_playing=True
    first_number= int(input("first number:"))
    math_op= input("math operator from +,-,*,/")
    second_number=int(input("second number:"))

    value=dict_operations[math_op](first_number,second_number)
    print(value)
    while keep_playing==True:
        print(keep_playing)
        keep_playing_question=input("keep playing?:")
        if keep_playing_question=="yes":
            first_number=value
            math_op = input("math operator from +,-,*,/")
            second_number = int(input("second number:"))
            value = dict_operations[math_op](first_number, second_number)
        elif keep_playing_question=="no":
            keep_playing=False
        print(value)
