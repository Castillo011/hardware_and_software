def check_number():
    number = input ("enter whole number:")
    try:
        return(true, int(number))
    except:
        print("invalid input!!")
        return(False, None)
def main ():
     good_selection = False 
     while not good_selection:
         good_selection, number = check_number()
     print("Good job", number ,"is a whole number" )