

def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print(f"{message} again")

