def conversation():
     print ("welcome to my conversation")
     print ("Do you like coding?")

     answer = input ("answer yes or no")
     if answer == "yes":
         print ("that's good")

     elif answer.lower() =="no":
        print("that's too bad!!")

     else:
         print ("That's too bad!!")
     print ("thanks for talking with me")

def main():
    conversation()
if __name__ == "__main__":
    main()
