def max(num1, num2):
     if num1 >= num2:
         print("1:",num1)
         return num1
     print("2:",num1)
     return num2 #(return) is to cleanup space in the stack so the system dont run out memory in the heap

def main():
     larger = max(1,5)
     print (larger)

if __name__ == "__main__":
        main()
