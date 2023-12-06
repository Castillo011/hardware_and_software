def stack_me(num1):
    if num1 == 0 | num1 == 10: # this mean that num1 is equal to 0 or equal 1
        print("add stack_me:", num1)
        print ("finished:",num1)
        return num1
    print ("add stack_me:" ,num1)
    num1 += 1
    return_me = stack_me(num1)
    print("remove stack_me:",num1,end=" " )
    print("return_me",return_me)

def main(): #def main is the fist part of the code that run
    start = 1 # start is the local variave that run next after def main (1)
    num1 = stack_me(start) #this run second(2)
    print("Back in main",end= " ")
    print('remove stack_me:', num1 )
if __name__ == '__main__':
    main()
