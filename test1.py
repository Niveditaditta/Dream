def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num%10) + str(reverse(num//10)))
    
def sum(num):
    if num<10:
        return num
    else:
        return num%10 + sum(num//10)
    
def execute(num):
    if num == reverse(num):
        print("Given number is a palindrome")
    else:
        print("Given number is a not palindrome") 

    total=sum(num)
    print(f"The sum of digits of the number is {total}")

n = ""
print(int(01))
while n != "exit":
  n = int(input("please give a number : "))
  execute(n)
