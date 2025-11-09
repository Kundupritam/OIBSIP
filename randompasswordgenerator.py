import random 
import string
#generating password
def generatepassword(length,letters,numbers,symbols):
    text=''
    password=''
    if letters:
        text=text+string.ascii_letters
    if numbers:
        text=text+string.digits
    if symbols:
        text=text+string.punctuation
    if not text:
        print("__please select atleast one character type__")
        return
    
    for _ in range(length):
        password=password+random.choice(text)
    return password

def main():
    print("__HELLO I AM A PASSWORD GENERATOR__")
    length=int(input("enter the length of the password:"))
    if length==0:
        print("please enter a positive integer")
        return
    letters=input("use letters?(y/n):").strip().lower()=='y'
    numbers=input("use numbers?(y/n):").strip().lower()=='y'
    symbols=input("use symbols?(y/n):").strip().lower()=='y'
    password=generatepassword(length,letters,numbers,symbols)
    if password is None:
        return

    print(f"your password is: {password}")
if __name__=="__main__":
    main()
   