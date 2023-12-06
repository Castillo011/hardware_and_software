def print_meters_to_cm (meters):
    print(100 * meters) #print will go the cpu and it will dysplay on screen and it will be remove from stack

def return_meters_to_cm(meters):
    return 100 * meters #return will go to the cpu and go back to the line it was call from and keep going

def main():
        return_cm = return_meters_to_cm(3)
        print(return_cm)
if __name__ == "__main__":
    main()
#Nope mean undefine
