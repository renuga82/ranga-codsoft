import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(characters)for i in range(length))
    return password
def main():
    try:
        length=int(input("enter the length of the password:"))
        if length<=0:
            print("please enter a positive integer:")
            return
        password=generate_password(length)
        print("generated password:",password)
    except ValueError:
        print("please enter a valid integer for the length")
if __name__=="__main__":
    main()
