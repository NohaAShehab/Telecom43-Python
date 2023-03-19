
def askfornum(message):
    while True:
        try:
            num = input(message)
            num = int(num)
        except Exception as e:
            print("---- invalid value , please enter it again")
        else:
            return num

def divnums():
    num1 = askfornum("please enter num1 : ")
    num2 = askfornum("please enter num2 : ")
    if num2==0:
        # raise  Exception("Invalid operation ---> Divsion by Zero ---- ")
        raise  ZeroDivisionError("Invalid operation ---> Divsion by Zero ---- ")

    print(f"num1 = {num1}, num2= {num2}")
    print("--- The division is being processed ----> ")
    res = num1/ num2
    print(res)

divnums()
