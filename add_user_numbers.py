Var = 42 

def add(num):
    return( num + Var )

def main():
    user1 = int(input("Enter a number:"))
    user2 = int(input("Enter another number:"))
    total = user1 + user2 

    number = add(total )
    print ("sum:", number)
    print ("Global:", Var)

if __name__ == '__main__':
    main()