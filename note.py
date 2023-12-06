def main():
    print ("Select one of the fallowing options:")
    print ("(A). Decimal to Binary")
    print ("(B). Binary to Decimal")
   
    
    answer = input("Please Enter your selection:").upper()
    
    if answer == "A":
       u

       

    if answer == "B":
     binary = input("Enter a binary number: ")
    decimal = binary_to_decimal(binary) 
    print(decimal)
    

def decimal_to_binary(n):
  binary = ""
  while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n //= 2
  return binary
    
def binary_to_decimal(binary):
  decimal = 0
  for digit in binary:
    decimal = decimal * 2 + int(digit)
  return decimal



 









if __name__ == '__main__':
    main()
   
  