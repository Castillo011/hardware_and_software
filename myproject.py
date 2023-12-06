from cgi import print_arguments


def main():
    print ("Select one of the fallowing options:")
    print ("(A). Decimal to Binary")
    print ("(B). Binary to Decimal")
   
    
    answer = input("Please Enter your selection:").upper()
    
    if answer == "A":
      decimal_number = int(input(" Please enter your DECIMAL number: "))
      binar_number = decimal_to_binary(decimal_number)
      print(f"The binary representation of {decimal_number} is {binar_number}")
      print("Will you like to return to the main menu?")
      usrChoice = int(input("Insert a -1 if you want to quit a 1 if you want to return to menu "))
      if(usrChoice == 1):
         return main()
      elif(usrChoice == -1):
         print("Thank you for using the converter")
      else:
         print("Wrong input going back to menu")
         return main()
       

    if answer == "B":
      binary = input("Please enter a BINARY number: ")
      decimal = binary_to_decimal(binary) 
      print(f"The decimal representation of {binary} is {decimal}")

      userChoice = int(input("Insert a -1 if you want to quit a 1 if you want to return to menu "))
      if(usrChoice == 1):
         return main()
      elif(userChoice == -1):
         print("Thank you for using the converter")
      else:
         print("Wrong input going back to menu")
         return main()
     
    
def binary_to_decimal(binary):
  decimal = 0
  for digit in binary:
    decimal = decimal * 2 + int(digit)
  return decimal

def decimal_to_binary(n):
  binar = ""
  while n > 0:
    remainder = n % 2
    binar = str(remainder) + binar
    n //= 2
  return binar

if __name__ == '__main__':
    main()
   
  
  
  

   
