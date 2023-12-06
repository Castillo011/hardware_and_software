def choose_a_door():
    prize = 4
    msg =  "choose the correct door 1, 2, 3: "
    print ("Do you want to win a prize?")
    # print statement tell the computer to display the msg
    door = int(input(msg))

    while door< 1 or door > 3:
        #"while" statement is the loupe" this mean that if i type the wrong answer is going to ask me to do it again.
         print ("Invalid Door!")
         door = int(input(msg))
    if door ==1:
        prize = 2 + 9 // 10 * 100
    elif door ==2 :
        prize += 6
    elif door == 3:
        for i in range (door):
            prize += i
    print ("you won " + str(prize) + " tickets!")
def main():
    choose_a_door()
if __name__ == "__main__":
        main()
