import os




def stop():
    return os.system("shutdown -a")
def shutdown():
    return os.system(f"shutdown /s /t {n}")
def restart():
    return os.system(f"shutdown /r /t {n}")
def uhd():
    ch = input("ENTER YOUR CHOICE(1 - shutdown, 2 - restart, 3 - to exit): ")


    if ch == "1":
        print(f"shutdown will happen in {n} seconds")
        shutdown()
        a = input("PRESS 0 TO CANCEL or any other key to exit: ")
        if a == "0":
            stop()
        else:
            exit()
        
    if ch == "2":
        print(f"shutdown will happen in {n} seconds")
        restart()
        a = input("PRESS 0 TO CANCEL or any other key to exit: ")
        if a == "0":
            stop()
        else:
            exit()

    if ch == "3":
        exit()
    else:
        print("ENTER CORRECT OPTION")
        uhd()




n = int(input("ENTER NUMBER OF SECONDS: "))
uhd()

