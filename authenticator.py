def user_info():
    db = open("users.py","r")
    info = []
    for i in db:
        pn,job,vac,covid,vacs,vacapt1,vacapt2,vacl = i.split(", ")
        info.append(pn)
        info.append(vac)
        info.append(covid)
        info.append(vacs)
        info.append(vacapt1)
        info.append(vacapt2)
        info.append(vacl)
    data = (pn,job,vac,covid,vacs,vacapt1,vacapt2,vacl)
    print(data)

def signup():
    db = open("PasswordDatabase.txt","r")
    Username = input("Create Username: ")
    Password = input("Create Password: ")
    Password1 = input("Confirm Password: ")
    name =[]
    password = []
    for i in db:
        nm,pas = i.split(", ")
        pas = pas.strip()
        name.append(nm)
        password.append(pas)
    data = dict(zip(name, password))


    if Password != Password1:
        print("Passwords don't not match\nTry again")
        signup()
    else:
        if Username in name:
            print("This user already exists\nTry again")
            signup()
        else:
            db = open("PasswordDatabase.txt", "a")
            db.write("\n"+Username+", "+Password)
            print("Sign up successful")


def access():
    db = open("PasswordDatabase.txt", "r")
    Username = input("Enter Username: ")
    Password = input("Enter Password: ")
    if not len(Username or Password) < 1:
        name =[]
        password = []
        for i in db:
            nm,pas = i.split(", ")
            pas = pas.strip()
            name.append(nm)
            password.append(pas)
        data = dict(zip(name, password))
        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login successful")
                        print("Welcome,",Username)
                        option = int(input("1.View Info\n>>"))
                        db = open("users.py","r")
                        info = []
                        for i in db:
                            pn,job,vac,covid,vacs,vacapt1,vacapt2,vacl = i.split(", ")
                            info.append(pn)
                            info.append(vac)
                            info.append(covid)
                            info.append(vacs)
                            info.append(vacapt1)
                            info.append(vacapt2)
                            info.append(vacl)
                        data = (pn,job,vac,covid,vacs,vacapt1,vacapt2,vacl)
                        if Username == "Alex":
                            print(data)
                        elif Username == "John":
                            print(data)
                    else:
                        print("Incorrect username or password")
                except:
                    print("Incorrect username or password")
            else:
                print("User doesn't exist")
        except:
            print("User doesn't exsist")


def main_menu(option = None):
    option = int(input("1.Login\n2.Sign Up\n>>"))
    if option == 1:
        access()
    elif option == 2:
        signup()
    else:
        print("Please enter a number to proceed")

main_menu()
