import string
import random

def display_menu():
    menu = """
******************************
*                            *
*           WELCOME          *
*            TO              *
*          PASSWORD          *
*          GENERATOR         *
*                            *
*                            *
******************************
*       Press Enter        *"""
    print(menu)


def display_pass(p):
    
    password_line = "{:^28}".format(p) 
    emoji= "\U0001F648".center(28, ' ') 
    Show_pass = f"""
    ******************************
 
                YOUR             
              PASSWORD          
    {emoji}
    {password_line}
   
    ******************************"""
    print(Show_pass)
    print("Press Enter For Menu")


display_menu()

def generate_pass(l,c):
    characters = " "
    p=[]
    p1= string.ascii_lowercase
    p2=string.ascii_uppercase
    p3=string.digits
    p4=string.punctuation
    if c == 1:
        p.extend(list(p1))
        characters += ''.join(p)

    elif c==2:
        p.extend(list(p1))
        p.extend(list(p2))
        

        characters += ''.join(p)
    elif c==3:
        p.extend(list(p1))
        p.extend(list(p2))
        p.extend(list(p3))


        characters += ''.join(p)



    elif c==4:
        p.extend(list(p1))
        p.extend(list(p2))
        p.extend(list(p3))
        p.extend(list(p4))
        characters += ''.join(p)
    password = ''.join(random.choice(characters) for _ in range(l))
    password = password.replace(" ", "") 
    display_pass(password) 

def com_show():
    print("\n")
    print("\n")
    print("Complexity Levels:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Extreme")
 

def main():  
        user_input = input()
        try:
            if user_input == '':
                print("1.Generate password")
                print("2. Exit")
                user_input2=int(input())
                if user_input2==1:
                    plen=int(input("Enter length of password\n"))
                    if plen>=8:
                        com_show()
                        print("Enter complexity of password\n")
                        cpass= int(input())
                        generate_pass(plen,cpass)
                        main()
                          

                    else:
                        print("The password must be at least 8 characters... To Contiue Enter\n")
                        main()
                else:
                    print("bye have a nice day")
        except:
            print("wrong input")
if __name__ == "__main__":
    main()