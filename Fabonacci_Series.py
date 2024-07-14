def fibonacci_nth_term(num):
  f1,f2=0,1
  f=0
  for i in range(num-2):
    f=f1+f2
    f1=f2
    f2=f
  print(f"The {num}th term of the sequence is {f}") 
   
def fibonacci_first_n_terms(num):
  f1,f2=0,1
  print(f"The sequence is {f1},{f2}",end=" ")
  for i in range(num-2):
    f=f1+f2
    f1=f2
    f2=f
    print(f,end=" ")
  print()

def fibonacci_between_m_and_n(m, n):
    f1,f2=0,1
    f=0
    print(f"THe sequence between {m} and {n} is",end=" ")
    while True:
      f=f1+f2
      if f>=n:
        break
      if f>m:
        print(f,end=" ")
      f1=f2
      f2=f
    print()  

def main():
  while True: 
   while True:
    print("1.Display n term of fabonacci sequence:")
    print("2.Display the first n fabonnaci numbers:")
    print("3.Display fabonacci sequence between m and n:")
    choice=int(input("Select your choice:"))
    if choice!=1 and choice!=2 and choice!=3:
       print("Select a valid choice:")
    else:
      break
   if choice == 1:
     num = int(input("Enter the number:"))
     fibonacci_nth_term(num)
   elif choice == 2:
     num = int(input("Enter the number of terms till you want to continue the sequence:"))
     fibonacci_first_n_terms(num)
   elif choice == 3:
      m = int(input("Enter the number where the range starts:"))
      n = int(input("Enter the number where the range ends:"))
      fibonacci_between_m_and_n(m, n)
   ch=input("Press y to continue:")
   if ch.lower()!='y':
     break

if __name__=="__main__":
  main()