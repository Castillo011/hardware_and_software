var = 42

def ask_me():
    num = int(input("Enter a number:"))
    return(num)


def main():
    global var 
    number1 = ask_me()
    number2 = ask_me()
    sum = 0
    sum +=(number2)
    sum += (number1)
    sum += (var)
    print ("sum:", sum)
    print ("globals",var)

if __name__ == '__main__':
    main()